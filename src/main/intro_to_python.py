#COT4500 Intro Assignment

import numpy as np

#creates a 3x3 matrix where cell is 1 if i=j, 0 if not
def create_first_matrix():
    matrix = np.array([[0,0,0],[0,0,0],[0,0,0]])
    i = 0
    j = 0

    while i < 3:
        j = 0

        while j < 3:
            if i==j:
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0
            j += 1

        i += 1

    return matrix

#add 3 where i does not equal j
def create_second_matrix(og_matrix):
    i = 0
    j = 0

    new_matrix = og_matrix
    for row in new_matrix:
        j=0

        for column in row:
            if i != j:
                new_matrix[i][j] += 3

            j+=1
        i+=1

    return new_matrix

#delete third column of matrix
def create_third_matrix(og_matrix):
    new_matrix = og_matrix

    new_matrix = np.delete(new_matrix, 2, 1)

    return new_matrix




matrix1 = create_first_matrix()
print(matrix1)

matrix2 = create_second_matrix(matrix1)
print(matrix2)

matrix3 = create_third_matrix(matrix2)
print(matrix3)
