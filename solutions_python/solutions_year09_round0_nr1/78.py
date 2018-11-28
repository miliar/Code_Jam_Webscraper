import sys, re

(l, d, n) = tuple([int(x) for x in sys.stdin.readline().split()])
s = []
for i in range(d):
    s.append(sys.stdin.readline())

for i in range(n):
    t = sys.stdin.readline().replace("(", "[").replace(")", "]")

    r = re.compile(t)
    res = 0
    for x in s:
        if re.match(r, x):
            res += 1
    print "Case #%d: %d" % (i + 1, res)
