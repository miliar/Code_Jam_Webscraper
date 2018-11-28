#!/usr/bin/env python

fin = open("1.in", "r")
fout = open("1.out", "w")

T = int(fin.readline())
for t in range(T):
    print str(t+1)
    R, C = map(int, fin.readline().split())
    rect = []
    for i in range(R):
        row = list(fin.readline())
        rect.append(row)

    for i in range(R):
        cur = '?'
        for j in range(C):
            if rect[i][j] != '?':
                cur = rect[i][j]
                break

        for j in range(C):
            if rect[i][j] != '?':
                cur = rect[i][j]
            else:
                rect[i][j] = cur

    for i in range(C):
        cur = '?'
        for j in range(R):
            if rect[j][i] != '?':
                cur = rect[j][i]
                break

        for j in range(R):
            if rect[j][i] != '?':
                cur = rect[j][i]
            else:
                rect[j][i] = cur

    ans = map(lambda x: ''.join(x), rect)
    fout.write("Case #" + str(t+1) + ":\n")
    for r in ans:
        fout.write(r)
