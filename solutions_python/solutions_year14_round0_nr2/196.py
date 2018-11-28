
import sys
in_ = sys.stdin

T = int(in_.readline())
for t in xrange(T):
    C, F, X = map(float, in_.readline().split(' '))
    rate = 2.0
    time, best = 0.0, X / rate
    while time < best:
        time += C / rate
        rate += F
        best = min(best, time + X / rate)
    print 'Case #%d: %.8f' % (t + 1, best)
