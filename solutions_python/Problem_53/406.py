def solve(f):
    N, K = map(int, f.readline().split())
    if (K+1) % (2**N) == 0:
        return "ON"
    else:
        return "OFF"

with open('A-large.in', 'r') as f:
    N = int(f.readline())
    results = [solve(f) for i in xrange(N) ]
    for i in xrange(N):
        print "Case #%d: %s" % (i+1, results[i])