import sys

if len(sys.argv) > 1:
    sys.stdin = open(sys.argv[1])

for test in range(input()):
    print "Case #{}:".format(test+1),

    N, K = map(int, raw_input().split())

    small, big = 1, 0

    bits = K.bit_length()-1

    for i in xrange(bits):
        increment = small + big

        if N & 1:
            small += increment
        else:
            big += increment

        N = (N-1) >> 1

    if K - (1 << bits) < big:
        N += 1

    print N/2, (N-1)/2
