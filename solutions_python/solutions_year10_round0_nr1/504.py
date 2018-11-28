#!/usr/bin/env python

# nb tests
T = int(raw_input())

# process tests
for i in xrange(1, T+1):
    (N, K) = raw_input().split(" ")
    N = int(N)
    K = int(K)

    state = ""
    if ((K - (pow(2, N) - 1)) % pow(2, N) == 0):
        state = "ON"
    else:
        state = "OFF"

    print "Case #" + str(i) + ": " + state
