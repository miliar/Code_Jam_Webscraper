import sys

T = int(sys.stdin.readline())
for case in xrange(T):
    N, K = [int(x) for x in sys.stdin.readline().split(' ')]

    if K % 2**N == 2**N - 1: ret = "ON"
    else: ret = "OFF"

    print "Case #{0}: {1}".format(case+1, ret)