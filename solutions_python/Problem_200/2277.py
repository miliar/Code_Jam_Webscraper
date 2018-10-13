#! /usr/bin/python3

def helper(s):
    if len(s) == 1:
        return s
    h = [x for x in s]
    h.sort()
    if s == ''.join(h):
        return s
    next = int(s[:-1])-1
    if next == 0:
        return '9'
    return helper(str(next))+'9'

T = int(input())
for t in range(1, T+1):
    s = input().strip()
    r = helper(s)
    print('Case #%d: %s' % (t, r))