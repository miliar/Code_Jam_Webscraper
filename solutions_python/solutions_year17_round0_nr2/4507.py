#!/usr/bin/env python2

from sys import stdin

lines = [int(x.strip()) for x in stdin.readlines()]
T = lines[0]
curr_line = 1

for t in xrange(1,T+1):
    ans =0
    num = lines[t]
    # print num
    digits = map(int, str(num))
    digits_str = str(num)

    repeated_start = 0
    valid = True
    for i in xrange(1, len(digits)):
        if(i > 1):
            if(digits[i-1] != digits[i-2]):
                repeated_start = i-1
        if digits[i] < digits[i-1]:
            valid = False
            # print "break",i
            break

    # print "Start", repeated_start

    if(not valid):
        # ans = num - int(''.join(digits_str[repeated_start+1:])) - 1
        ans = num - 1
        tmp = 1
        # for i in reversed(xrange(repeated_start+1, len(digits))):
        for i in xrange(0, len(digits)-repeated_start-1):
        # for i in xrange(repeated_start+1, len(digits)):
            # ans -= tmp*digits[len(digits)-i+1]
            # ans -= tmp*digits[i]
            ans -= tmp*digits[len(digits)-i-1]
            # print len(digits)-i-1, digits[len(digits)-i-1], tmp
            tmp *= 10
    else:
        ans = num

    print "Case #%d: %d" % (t, ans)
