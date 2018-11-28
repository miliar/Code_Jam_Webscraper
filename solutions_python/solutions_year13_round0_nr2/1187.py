#!/usr/bin/python


def check2(row, col, X, Y, N, M):
    crow = int(row[Y])
    ccol = int(col[X])
    pfound = 0
    for i in range(0, M):
        if crow < int(row[i]):
            pfound += 1
            break
    for j in range(0, N):
        if ccol < int(col[j]):
            pfound += 1
            break
    if pfound == 2:
        return 'NO'
    return 'YES'


def convertcol(l, N, M):
    l2 = []
    l3 = []
    for j in range(0, M):
        for i in range(0, N):
            try:
                l2.append(l[i][j])
            except:
                l2 = []
                l2.append(l[i][j])
        l3.append(l2)
        l2 = []
    return l3


def check(N, M, lX):
    if N < 2 or M < 2:
        return 'YES'
    lY = convertcol(lX, N, M)
    for i in range(0, N):
        for j in range(0, M):
            res = check2(lX[i], lY[j], i, j, N, M)
            if res == 'NO':
                return 'NO'
    return 'YES'

lines = {}
counter = 0
loopcounter = 0
T = 0
NextSplit = 0
for line in open('inp', 'r'):
    line = line.strip()
    if counter == 0:
        T = int(line)
        counter += 1
        loopcounter += 1
        continue
    if loopcounter == NextSplit + 1:
        N, M = line.split()
        lines[str(counter) + 'N'] = N
        lines[str(counter) + 'M'] = M
        NextSplit = loopcounter + int(N)
        counter += 1
        loopcounter += 1
        continue
    else:
        try:
            lines[counter - 1].append(line.split())
        except:
            lines[counter - 1] = [line.split()]
    loopcounter += 1


counter = 1
result = []
while counter <= T:
    #print counter
    res = check(int(lines[str(counter) + 'N']), int(lines[str(counter) + 'M']),
                lines[counter])
    result.append(res)
    counter += 1

counter = 0
file = open('out', 'w')
while counter < T:
    file.write('Case #' + str(counter + 1) + ': ' + result[counter] + '\n')
    counter += 1
