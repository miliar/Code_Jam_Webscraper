#Read Input - Absolutely 0 input checks

import fileinput

infile = fileinput.input()

p = infile.readline()

T = long(p)

t = 0

while t < T:
    t += 1
    total = 0
    p = infile.readline()
    p = infile.readline()
    C = [long(x) for x in p.split()]
    N = len(C)
    n = 0
    while (n < N):
        total ^= C[n]
        n += 1
    if total == 0:
        print 'Case #%d: %d' % (t, sum(C) - min(C))
    else:
        print 'Case #%d: NO' % (t)
