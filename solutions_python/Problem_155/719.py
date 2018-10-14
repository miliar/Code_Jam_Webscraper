#!/usr/bin/env python

T = input()
for cas in xrange (T):
    line = raw_input ().split ()
    n, str = line[0], line[1]
    ans = 0
    sum = 0
    for c in str:
        sum += int(c)

    i = len (str) - 1
    while (i >= 0):
        sum -= int (str[i])
        if sum < i:
            ans += (i - sum)
            sum = i
        i -= 1
    print 'Case', '#%i:'%(cas+1), ans
