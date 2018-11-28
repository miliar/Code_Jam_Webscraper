#!/usr/bin/env python

num_tests = input()

for test_no in xrange(1, num_tests + 1):
    n, p = map(int, raw_input().split())
    g = map(int, raw_input().split())
    g = [i % p for i in g]

    ans = g.count(0)
    g = [i for i in g if i != 0]

    if p == 2:
        ans += (len(g) + 1) / 2
    elif p == 3:
        rem1 = g.count(1)
        rem2 = g.count(2)
        min12 = min(rem1, rem2)
        ans += min12
        rem1 -= min12
        rem2 -= min12
        
        ans += (rem1 + rem2 + 2) / 3

    elif p == 4:
        rem1 = g.count(1)
        rem2 = g.count(2)
        rem3 = g.count(3)
        
        min13 = min(rem1, rem3)
        ans += min13
        rem1 -= min13
        rem3 -= min13
        
        ans += rem2 / 2
        rem2 %= 2

        if rem2:
            if rem1 > 2:
                rem1 -= 2
                ans += 1
                ans += (rem1 + 3) / 4
            elif rem3:
                rem3 -= 2
                ans += 1
                ans += (rem3 + 3) / 4
            else: # Only 2 remains
                ans += 1
        else:
            if rem1 > 4:
                ans += (rem1 + 3) / 4
            elif rem3 > 4:
                ans += (rem3 + 3) / 4
            elif rem1 or rem3: # If at most 4 remain of rem1 or rem3
                ans += 1
    else:
        raise Exception('Unrecognised value for p: {0}'.format(p))

    print 'Case #{0}: {1}'.format(test_no, ans)
