from collections import deque as Queue


def solve(g):
    rowmaxes = [max(row) for row in g]

    colmaxes = [max([row[i] for row in g]) for i in range(len(g[0]))]

    for i in range(len(g)):
        for j in range(len(g[i])):
            val = g[i][j]
            #print val, rowmaxes[i], colmaxes[j]
            if val < rowmaxes[i] and val < colmaxes[j]:
                return 'NO'


    return 'YES'


inp = raw_input()
T = int(inp)
for t in range(1,T+1):
    inp = raw_input()
    N, M = map(int, inp.split(' '))
    grid = []
    for i in range(N):
        inp = raw_input()
        row = map(int, inp.split(' '))
        grid.append(row)
    answer = solve(grid)
    print "Case #" + str(t) + ": " + str(answer)
