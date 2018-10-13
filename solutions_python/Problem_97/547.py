import sys

def rotations(x):
    s = str(x)
    r = []
    for i in xrange(1, len(s)):
        t = s[i:] + s[:i]
        y = int(t)
        if not y in r:
            r.append(int(t))
    return r

def f(start, end):
    num = 0
    for i in xrange(start, end + 1):
        s = i
        for r in rotations(s):
            if s < r <= end:
                num += 1
    return num

lines = sys.stdin.readlines()
idx = 0
for l in lines[1:]:
    start, end = map(int, l.split())
    idx += 1
    print "Case #{}: {}".format(idx, f(start, end))

