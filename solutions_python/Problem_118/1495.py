import math
def isPal(x):
    sx = str(x)
    for i in range(len(sx) / 2 + 1):
        if sx[i] != sx[len(sx) - i - 1]:
            return False
    return True

n, = map(int, raw_input().split())
for i in range(1, n + 1):
    ct = 0
    a, b = map(int, raw_input().split())
    for x in xrange(int(math.ceil(math.sqrt(a))), int(math.floor(math.sqrt(b))) + 1):
        if isPal(x) and isPal(x * x):
            ct += 1
    print 'Case #{}: {}'.format(i, ct)