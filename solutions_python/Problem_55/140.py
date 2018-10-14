def solve(R, k, groups):
    q = groups[:]
    money = 0
    for _ in xrange(R):
##        print "_"*10
        riders = []
        left = k
        while True:
##            print q, riders
            if not q:
                break
            if q[0] > left:
                break
            riders.append(q[0])
            left -= q.pop(0)
        money += sum(riders)
        q = q + riders
    return money

import sys

if __name__ == "__main__":
    f = sys.stdin
    T = int(f.readline())
    for t in xrange(T):
        R, k, N = map(int, f.readline().split())
        gs = map(int, f.readline().split())
        assert len(gs) == N
        print "Case #%d: %d" % (t+1, solve(R, k, gs))
