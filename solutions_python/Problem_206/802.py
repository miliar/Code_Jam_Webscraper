import sys

T = int(sys.stdin.readline())

for t in xrange(T):
    D, N = [int(x) for x in sys.stdin.readline().strip().split(' ')]
    K = []
    S = []

    for _ in xrange(N):
        k, s = [int(x) for x in sys.stdin.readline().strip().split(' ')]
        K.append(k)
        S.append(s)

    max_time = 0
    for n in xrange(N):
        max_time = max(max_time, (float(D - K[n])) / S[n])

    print "Case #%d: %.6f" % (t + 1, D / max_time)
