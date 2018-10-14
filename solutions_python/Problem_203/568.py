#
# IMPORTS
#
import fileinput

data = fileinput.input()
t = int(data[0])

l = 1
for i in range(1, t + 1):
    line = data[l].split()
    r = int(line[0])
    c = int(line[1])

    matrix = []
    for j in range(1, r + 1):
        line = data[l + j]
        matrix.append(list(line.split()[0]))
    l = l + r + 1

    for j in range(0, r):
        for k in range(0, c):
            if k is not c - 1 and matrix[j][k + 1] is '?' :
                matrix[j][k + 1] = matrix[j][k]
            elif k is not 0 and matrix[j][k - 1] is '?':
                matrix[j][k - 1] = matrix[j][k]
    for j in range(r - 1, -1, -1):
        for k in range(c - 1, -1, -1):
            if k is not c - 1 and matrix[j][k + 1] is '?' :
                matrix[j][k + 1] = matrix[j][k]
            elif k is not 0 and matrix[j][k - 1] is '?':
                matrix[j][k - 1] = matrix[j][k]
    for k in range(0, c):
        for j in range(0, r):
            if j is not r - 1 and matrix[j + 1][k] is '?' :
                matrix[j + 1][k] = matrix[j][k]
            elif j is not 0 and matrix[j - 1][k] is '?':
                matrix[j - 1][k] = matrix[j][k]
    for k in range(c - 1, -1, -1):
        for j in range(r - 1, -1, -1):
            if j is not r - 1 and matrix[j + 1][k] is '?' :
                matrix[j + 1][k] = matrix[j][k]
            elif j is not 0 and matrix[j - 1][k] is '?':
                matrix[j - 1][k] = matrix[j][k]


    print('Case #{}: '.format(i))
    for j in range(0, r):
        print ''.join(matrix[j])
