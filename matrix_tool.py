import numpy as np

def input_matrix():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of cols: "))
    print("Enter elements row-wise:")
    matrix = []
    for i in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)
    return np.array(matrix)

print("Matrix 1:")
A = input_matrix()

print("Matrix 2:")
B = input_matrix()

print("\nAddition:\n", A + B)
print("\nSubtraction:\n", A - B)

if A.shape[1] == B.shape[0]:
    print("\nMultiplication:\n", np.dot(A, B))
else:
    print("\nMultiplication not possible")

print("\nTranspose of A:\n", A.T)

if A.shape[0] == A.shape[1]:
    print("\nDeterminant of A:", np.linalg.det(A))
else:
    print("\nDeterminant not possible")
