import random

def fill_matrix_random(matrix):
    matrix[:] = [[random.randint(0, 100) for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
