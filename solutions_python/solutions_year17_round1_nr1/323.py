import os, sys

infn = raw_input('filename?\n')
inf = open(infn)
inp = inf.read().split('\n')
inf.close()

T = int(inp.pop(0))

outf = open('output','w')
for i in range(T):
    R, C = [int(x) for x in inp.pop(0).split(' ')]
    cake = list()
    for r in range(R):
        cake.append(list(inp.pop(0)))
    if i == 42:
        print cake
    for r in range(R):
        for c in range(C):
            if cake[r][c] != '?':
                initial = cake[r][c]
                for max_c in range(c+1,C):
                    if cake[r][max_c] != '?':
                        max_c -= 1
                        break
                if c == C-1:
                    max_c = c
                print max_c, initial
                for row in range(r+1):
                    for col in range(max_c+1):
                        if cake[row][col] == '?':
                            cake[row][col] = initial

    for r in range(R):
        for c in range(C):
            if cake[r][c] == '?':
                for row in range(r,0,-1):
                    if cake[row-1][c] != '?':
                        cake[r][c] = cake[row-1][c]
                        break
    outf.write('Case #{0}:\n'.format(i+1))
    for r in range(R):
        outf.write('{0}\n'.format(''.join(cake[r])))
outf.close()