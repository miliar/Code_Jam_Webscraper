#!/usr/bin/python

def update_prefix(digit, k, n):
    for i in xrange(k, 0, -1):
        if digit[i] < digit[i-1]:
            digit[i-1] -= 1
            digit[i] = 9

def update_suffix(digit, k, n):
    digit[k:n] = [9] * (n-k)

def solve(case_no):
    digit = map(int, list(raw_input()))
    n = len(digit)
    
    for i in xrange(1, n):
        if digit[i] < digit[i-1]:
            update_prefix(digit, i, n)
            update_suffix(digit, i, n)
            break

    ans = int(''.join(map(str, digit)))
    print 'Case #%d: %d' % (case_no, ans)

t = int(raw_input())
for case_no in xrange(1, t+1):
    solve(case_no)
