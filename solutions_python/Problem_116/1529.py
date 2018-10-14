import sys

def solve(A):
    #print ''.join(A)
    for i in range(4):
        if sum(A[i][j] == 'X' or A[i][j] == 'T' for j in range(4)) == 4:
            return 'X won'
        if sum(A[i][j] == 'O' or A[i][j] == 'T' for j in range(4)) == 4:
            return 'O won'
        if sum(A[j][i] == 'X' or A[i][j] == 'T' for j in range(4)) == 4:
            return 'X won'
        if sum(A[j][i] == 'O' or A[i][j] == 'T' for j in range(4)) == 4:
            return 'O won'
    if sum(A[i][i] == 'X' or A[i][i] == 'T' for i in range(4)) == 4:
        return 'X won'
    if sum(A[i][i] == 'O' or A[i][i] == 'T' for i in range(4)) == 4:
        return 'O won'
    if sum(A[i][3-i] == 'X' or A[i][3-i] == 'T' for i in range(4)) == 4:
        return 'X won'
    if sum(A[i][3-i] == 'O' or A[i][3-i] == 'T' for i in range(4)) == 4:
        return 'O won'
    if any(A[i][j] == '.' for i in range(4) for j in range(4)):
        return 'Game has not completed'
    return 'Draw'

lines = sys.stdin.readlines()
for i in range(int(lines[0])):
    print 'Case #{0}: {1}'.format(i+1, solve(lines[5*i+1: 5*i+5]))

