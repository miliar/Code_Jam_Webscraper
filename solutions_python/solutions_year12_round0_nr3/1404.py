import sys

def rotate(s, n):
    if n <= 0: return s
    else: return rotate(s[-1] + s[:-1], n - 1)

def recycled(n, m):
    for i in xrange(len(str(n))):
        if rotate(n, i) == m: return True
    return False

#init
v = {}
for x in xrange(1, 1001):
    if x < 10: upper = 10
    if x < 100: upper = 100
    if x < 1000: upper = 1000
    else: upper = 1001
    for y in xrange(x + 1, upper):
        if recycled(str(x), str(y)):
            v[(x, y)] = True
        else:
            v[(x, y)] = False

f = open(sys.argv[1])
t = int(f.readline())
for _t in xrange(t):
    a, b = map(int, f.readline().split())
    c = 0
    for x in xrange(a, b):
        for y in xrange(x + 1, b + 1):
            if v[(x, y)]: c += 1
    print 'Case #%d: %d' % (_t + 1, c)
