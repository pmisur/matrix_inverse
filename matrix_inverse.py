# import numpy as np
from typing import List
import sys

class Matrix:
    rows: int
    cols: int
    elements: List[float]

    def __init__(self, rows: int, cols: int, elements: List[float]):
        self.rows = rows
        self.cols = cols
        self.elements = elements

    @property
    def determinant(self) -> float:
        if self.rows != self.cols:
            raise ValueError("Number of rows and coloumns must be equal!")

        represented_matrix = []
        for i in range(0, len(list), self.rows):
            represented_matrix.append(self.elements[i:i + self.rows])

        represented_matrix = [self.elements[i:i + self.rows]
                              for i in range(0, len(list), self.rows)]

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

    def add(m: 'Matrix') -> 'Matrix':
        pass

    @staticmethod
    def read_from_file(file, rows, cols) -> 'Matrix':   #should be able to read given part of the file
        matrix = Matrix(rows=rows, cols=cols, elements=[])
        with open(file) as f:
            line = next(f)
            for element in line.split(','):
                matrix.elements.append(int(element))

            line = next(f)
            for element in line.split(','):
                matrix.elements.append(int(element))


            for line in f:
                for element in line.split(','):
                    matrix.elements.append(int(element))
        return matrix

    @staticmethod
    def indentity(rows, cols) -> 'Matrix':
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


def main(argv):
    # print(indentity_matrix_generator(4,4).___repr___())
    print(Matrix.read_from_file('matrix.txt', 3, 3).___repr___())
    # print(indentity_matrix_generator(3,3).determinant)


if __name__ == '__main__':
    main(sys.argv)
