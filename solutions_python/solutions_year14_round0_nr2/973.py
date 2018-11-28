import math

T = input()

for i in xrange(T):
    print "Case #%d:" % (i + 1),
    c, f, x = map(float, raw_input().split())
    n = max(0, math.floor(x / c - 2 / f))
    result = 0
    for j in xrange(int(n)):
        result += c / (2 + j * f)
    result += x / (2 + n * f)
    print result

