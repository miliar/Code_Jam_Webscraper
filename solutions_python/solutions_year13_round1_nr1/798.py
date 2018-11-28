#!/usr/bin/python

import sys

def getNLines(r, t):
    result = 0
    havePaint = True
    t = t - (2 * r + 1)
    r += 2
    while t >= 0:
        result += 1
        t = t - (2 * r + 1)
        r += 2

    return result


fin = open(sys.argv[1], 'r')
fout = open(sys.argv[2], 'w')

ncases = int(fin.readline().strip())
i = 0
for line in fin:
    [r, t] = line.strip().split()
    r, t = int(r), int(t)
    result = getNLines(r, t)
    i += 1
    fout.write("Case #" + str(i) + ": " + str(result) + "\n")



fin.close()
fout.close()


