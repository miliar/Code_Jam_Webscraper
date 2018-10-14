#!/usr/bin/python

def read_input():
    line = raw_input().split(' ')
    return (line[0], int(line[1]))

def flip(s, idx, k):
    first = s[:idx]
    middle = s[idx:idx+k].replace('+', '?').replace('-', '+').replace('?', '-')
    last = s[idx+k:]
    return first + middle + last

def solve(case_no):
    s, k = read_input()
    n = len(s)
    count = 0

    for i in xrange(n-k+1):
        if s[i] == '-':
            s = flip(s, i, k)
            count += 1

    if s.count('+') == n:
        print 'Case #%d: %d' % (case_no, count)
    else:
        print 'Case #%d: IMPOSSIBLE' % (case_no, )

t = int(raw_input())
for case_no in xrange(1, t+1):
    solve(case_no)
