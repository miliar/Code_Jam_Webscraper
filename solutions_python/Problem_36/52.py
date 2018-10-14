import sys

fin = open(sys.argv[1] + '.in')
fout = open(sys.argv[1] + '.out', 'w')

pat = "welcome to code jam"

def solve():
    r = [0] * (len(pat) + 1)
    r[0] = 1
    for ch in fin.readline():
        r0 = r[:]
        for i, ch1 in enumerate(pat):
            if ch1 == ch:
                r[i + 1] = (r[i + 1] + r0[i]) % 10000
    return '%.4d' % r[len(pat)]

ccc = int(fin.readline())
for c in range(1, ccc + 1):
    print >>fout, "Case #%d: %s" % (c, solve())
