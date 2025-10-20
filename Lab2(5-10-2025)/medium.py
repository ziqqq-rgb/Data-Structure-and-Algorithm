def findPeakGrid(mat):
    n = len(mat)
    m = len(mat[0])

    for i in range(n):
        for j in range(m):
            curr = mat[i][j]
            isPeak = True

            # check top
            if i > 0 and mat[i - 1][j] > curr:
                isPeak = False

            # check bottom
            if i + 1 < n and mat[i + 1][j] > curr:
                isPeak = False

            # check left
            if j > 0 and mat[i][j - 1] > curr:
                isPeak = False

            # check right
            if j + 1 < m and mat[i][j + 1] > curr:
                isPeak = False

            if isPeak:
                return [i, j]

    return [-1, -1]


if __name__ == "__main__":
    mat = [
        [10, 20, 15],
        [21, 30, 14],
        [7, 16, 32]
    ]

    peak = findPeakGrid(mat)
    print(peak[0], peak[1])