#!/usr/bin/python

for case in range(input()):
    N = int(raw_input())
    candy = sorted([int(x) for x in raw_input().split()], reverse=True)
    xor_sum = 0
    for c in candy:
        xor_sum = xor_sum ^ c
    if xor_sum != 0:
        print "Case #%s: NO" % (case + 1)
    else:
        print "Case #%s: %s" % (case + 1, sum(candy[:-1]))
