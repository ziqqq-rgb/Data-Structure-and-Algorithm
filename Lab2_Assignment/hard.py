def booleanMatrix(mat):
    rows, cols = len(mat), len(mat[0])

    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 1:
                # Replace all the zeros in jth column by -1
                for idx in range(rows):
                    if mat[idx][j] == 0:
                        mat[idx][j] = -1

                # Replace all the zeros in ith row by -1
                for idx in range(cols):
                    if mat[i][idx] == 0:
                        mat[i][idx] = -1

    # Replace all the -1 by 1
    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == -1:
                mat[i][j] = 1

if __name__ == "__main__":
    mat = [[1, 0, 0, 1], [0, 0, 1, 0], [0, 0, 0, 0]]
    booleanMatrix(mat)
    for row in mat:
        print(" ".join(map(str, row)))