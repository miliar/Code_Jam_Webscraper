import sys
from array import array
def main():
    N = int(sys.stdin.readline())
    for case in xrange(N):
        S = int(sys.stdin.readline())
        engine = dict([(sys.stdin.readline(), i) for i in xrange(S)])
        Q = int(sys.stdin.readline())
        queries = [engine[sys.stdin.readline()] for i in xrange(Q)]
        dp_prev = array('i', [0 for x in xrange(S)])
        dp_next = array('i', [0 for x in xrange(S)])
        queries.reverse()
        for q in queries:
            for i in xrange(S):
                dp_next[i] = dp_prev[i] if i != q else min([dp_prev[j] for j in xrange(S) if j != i]) + 1
            dp_prev, dp_next = dp_next, dp_prev
        print 'Case #%d: %d' % (case + 1, min(dp_prev))
main()