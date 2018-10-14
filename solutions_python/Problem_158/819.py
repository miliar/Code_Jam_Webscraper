#!/usr/bin/env python2

T = input()
for t in range(1, T+1):
    X, R, C = map(int, raw_input().split())
    ans = 'RICHARD' # Can make it lose
    if X == 1:
        ans = 'GABRIEL'
    elif X == 2 and R*C%2==0:
        ans = 'GABRIEL'
    elif X == 3 and (R == 3 or C == 3) and (R*C > 3):
        ans = 'GABRIEL'
    elif X == 4 and (R,C) in [(3,4),(4,3),(4,4)]:
        ans = 'GABRIEL'

    print 'Case #' + str(t) + ': ' + ans
