from sys import stdin
import math

def solve(t):
    line = stdin.readline().split(' ')
    n = int(line[0])
    q = int(line[1])

    e = []
    s = []
    for i in range(0, n):
        line = stdin.readline().split(' ')
        ei = float(line[0])
        si = float(line[1])
        e.append(ei)
        s.append(si)

    d = []
    for i in range(0, n):
        temp = []
        line = stdin.readline().split(' ')
        for j in range(0, n):
            c = float(line[j])
            if c == -1:
                c = math.inf
            temp.append(c)
        d.append(temp)


    d1 = d.copy()
    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                temp = d1[i][k] + d1[k][j]
                d1[i][j] = min(d1[i][j], temp)

    d2 = d1.copy()
    for i in range(0, n):
        for j in range(0, n):
            ei = e[i]
            si = s[i]
            if ei >= d1[i][j]:
                d2[i][j] = d1[i][j] / si
            else:
                d2[i][j] = math.inf

    d3 = d2.copy()
    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                temp = d3[i][k] + d3[k][j]
                d3[i][j] = min(d3[i][j], temp)

    res = ''
    for i in range(0, q):
        line = stdin.readline().split(' ')
        uk = int(line[0]) - 1
        vk = int(line[1]) - 1
        res += str(d3[uk][vk]) + ' '

    print('Case #' + str(t + 1) + ': ' + res)

T = int(stdin.readline())
for t in range(0, T):
    solve(t)
