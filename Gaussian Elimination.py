# Gaussian elimination to reduce an n*n matrix to upper triangular form
# 14/08/25

import numpy as np

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

upper_triangular = matrix.copy()

for i in range(1,len(matrix)):
    for j in range(i):
        factor = matrix[i][j] / matrix[j][j]
        upper_triangular[i] = matrix[i] - factor * matrix[j]
print(upper_triangular)
