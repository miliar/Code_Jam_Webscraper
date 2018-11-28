#!/usr/bin/env python

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
T = int(raw_input())  # read a line with a single integer
for t in xrange(1, T + 1):
    s, k = raw_input().split(" ")
    k = int(k)
    count = 0
    chars = []
    for c in s:
        chars.append(c)
    possible = True
    for i in xrange(len(chars)):
        if chars[i] == '-':
            if i + k <= len(chars):
                for j in xrange(i, i + k):
                    if chars[j] == '-' :
                        chars[j] = '+'
                    else:
                        chars[j] = '-'
                count = count + 1
            else:
                possible = False
                break

    if possible:
        print "Case #{}: {}".format(t, count)
    else:
        print "Case #{}: IMPOSSIBLE".format(t)
