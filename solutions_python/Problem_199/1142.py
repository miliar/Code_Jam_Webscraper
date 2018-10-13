import sys

lines = open(sys.argv[1], "rb").read().splitlines()
res = ""

def flip(pp, i, k):
    d = { '-': '+', '+': '-' }
    for j in xrange(i, i + k):
        pp[j] = d[pp[j]]

for t, line in enumerate(lines[1:]):
    pp, k = line.split(' ')
    k = int(k)
    pp = list(pp)
    c = 0
    for i in xrange(len(pp) - k + 1):
        if pp[i] == '-':
            flip(pp, i, k)
            c += 1
    x = ""
    if pp.count('+') != len(pp):
        x = "IMPOSSIBLE"
    else:
        x = str(c)
    res += "Case #%d: %s\n" % (t + 1, x)

open(sys.argv[2], "wb").write(res)
