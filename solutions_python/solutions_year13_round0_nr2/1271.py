import sys
import re


inputf = open('in.txt', 'r')
outf = open('out.txt', 'w')

case = int(inputf.readline())

for case in range(1, case+1):
    outf.write("Case #%d: " % case)
    m = []
    (s,g) = map(int, inputf.readline().split(' '))
    #print (s,g)
    for i in range(s):
        m.append(map(int, inputf.readline().split(' ')))

    #print m

    totalSucc = True

    for (i,j) in [(i,j) for i in range(s) for j in range(g)]:
        r = True
        for k in range(s):
            if m[i][j] < m[k][j]:
                r = False
        c = True
        for k in range(g):
            if m[i][j] < m[i][k]:
                c = False

        if not (r or c):
            outf.write('NO\n')
            totalSucc = False
            break

    if totalSucc:
        outf.write('YES\n')
outf.close()
