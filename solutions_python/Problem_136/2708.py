import sys

T = int(sys.stdin.readline())
for t in range(T):
    c, f, x = map(float, sys.stdin.readline().split())
    rate, sofar, fcount = 2.0, 0.0, 0
    best = x / rate
    while sofar < best:
        sofar += c / rate
        fcount += 1
        rate += f
        best = min(best, sofar + x / rate)
    print 'Case #%d: %.10f' % (t+1, best)

