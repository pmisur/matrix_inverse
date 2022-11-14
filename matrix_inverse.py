import numpy as np

class Matrix:
    rows: int
    cols: int
    elements: list

    def __init__(self, rows:int, cols:int, elements:list):
        self.rows:int = rows
        self.cols:int = cols
        self.elements:list = elements

    @property
    def determinant(self) -> float:
        if self.rows != self.cols:
            raise ValueError("Number of rows and coloumns must be equal!")
        def func(list, n):
            for i in range(0, len(list), n):
                yield list[i:i + n]
        represented_matrix = (list(func(self.elements, self.rows)))
        determinant = np.linalg.det(represented_matrix)
        return determinant
   
    def ___repr___(self):
        print("\n")
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.elements[self.cols * i + j], end='   ')
            print("\n")

def read_matrix_from_file(file, rows, cols) -> Matrix:   #should be able to read given part of the file
    matrix = Matrix(rows=rows, cols=cols, elements=[])
    with open(file) as f:
        for element in next(f).split(','):
            matrix.elements.append(int(element))
        for line in f:
            for element in line.split(','):
                matrix.elements.append(int(element))
    return matrix


def indentity_matrix_generator(rows, cols) -> Matrix:
    if rows != cols:
        raise ValueError("Number of rows and coloumns must be equal!")
    matrix = Matrix(rows=rows, cols=cols, elements=[])
    for i in range(rows):
        for j in range(cols):
            if i == j:
                matrix.elements.append(1)
            else:
                matrix.elements.append(0)
    return matrix



print(indentity_matrix_generator(4,4).___repr___())
print(read_matrix_from_file('matrix.txt', 3, 3).___repr___())
print(indentity_matrix_generator(3,3).determinant)
