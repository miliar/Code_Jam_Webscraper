import sys
import string

filename = sys.argv[1]
f = open(filename, "r")
lines = map(string.strip, f.readlines())
T = int(lines[0])

lines = lines[1:]

for t in range(T):
    N = int(lines[t * 2])
    M = map(int, lines[(t *  2) + 1].split())

    y = 0
    for i, m in enumerate(M):
        if i + 1 < len(M):
            n = M[i + 1]
            if m - n >= 0:
                y += m - n

    rate = 0
    for i in range(len(M) - 1):
        m1 = M[i]
        m2 = M[i+1]
        if m1 - m2 >= rate:
            rate = m1 - m2
    
    if rate <= 0:
        z = 0
    else:
        z = 0
        for m in M[:-1]:
            if m <= rate:
                z += m
            else:
                z += rate

    print "Case #%s: %s %s" % (t + 1, y, z)
