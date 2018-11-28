#!/usr/bin/python

#
# Wow, if this passes it would be the first program I got right without needing any debugging...
#
def istidy_s(s):
    return all(s[i] <= s[i+1] for i in range (len(s) - 1))

def istidy(n):
    return istidy_s(str(n))

T = int(raw_input())
for c in range(1, T+1):
    N = int(raw_input())
    while not istidy(N):
        for i in range(20):
            if (N / 10**i) % 10 != 9:
                N = (N / 10**(i+1)) * 10**(i+1) - 1
                break

    print "Case #%d: %d" % (c, N)

