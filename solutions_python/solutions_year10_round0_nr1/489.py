#! /usr/bin/python
'''
Snappr
'''

T = int(raw_input())

for i in range(T):
    n, k = map(int, raw_input().split())
    if k % (2 ** n) == 2 ** n - 1:
        ans = 'ON'
    else:
        ans = 'OFF'
    print 'Case #%d: %s' % (i + 1, ans)
