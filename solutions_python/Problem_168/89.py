#!/usr/bin/python2.7


f = open('input.txt', 'r')
T = int(f.readline())

e = 0
l = 1
r = 2
u = 3
d = 4

def column(matrix, i):
    return [row[i] for row in matrix]

def willOffGrid(mat, i, j, direction):
    arr = []
    if direction == l:
        arr = mat[i][:j]
    elif direction == r:
        arr = mat[i][(j + 1):]
    elif direction == u:
        arr = column(mat, j)[:i]
    elif direction == d:
        arr = column(mat, j)[(i + 1):]

    for char in arr:
        if char != e:
            return False

    return True

def solve(mat, r, c):
    count = 0

    for i in range(r):
        for j in range(c):
            char = mat[i][j]
            if char != e:
                if willOffGrid(mat, i, j, char):
                    possible = False
                    for direction in range(1, 5):
                        if direction != char and not willOffGrid(mat, i, j, direction):
                            possible = True
                            break
                    if possible:
                        count += 1
                    else:
                        return -1

    return count

for t in range(T):
    R, C = map(int, f.readline().rstrip().split(' '))
    mat = []
    for i in range(R):
        mat.append([])
        arr = f.readline().rstrip()
        assert C == len(arr)
        for j in range(C):
            char = arr[j]
            if char == '.':
                mat[i].append(e)
            elif char == '^':
                mat[i].append(u)
            elif char == 'v':
                mat[i].append(d)
            elif char == '<':
                mat[i].append(l)
            elif char == '>':
                mat[i].append(r)
            else:
                raise ValueError('Illegal input.')

    print "Case #" + str(t + 1) + ":",
    num = solve(mat, R, C)
    if num != -1:
        print num
    else:
        print 'IMPOSSIBLE'

