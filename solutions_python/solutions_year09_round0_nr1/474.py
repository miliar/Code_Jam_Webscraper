import sys, re

line = sys.stdin.readline()
L, D, N = [int(x) for x in line.split()]

words = []
for i in xrange(0, D):
    line = sys.stdin.readline().strip()
    words.append(line)

words.sort()

cases = 1
for i in xrange(0, N):
    pat = sys.stdin.readline().strip().replace("(", "[").replace(")", "]")
    m = re.compile(pat)
    res = 0
    for w in words:
        if m.match(w) != None:
            res += 1
    print "Case #%d: %d" % (cases, res)
    cases += 1
