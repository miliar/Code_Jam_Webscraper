#!/usr/bin/env python

def flip(s):
    ret = ''
    for i in s:
        if i == '-':
            ret += '+'
        else:
            ret += '-'
    return ret

for _ in xrange(input()):
    s, k = raw_input().split()
    k = int(k)
    l = list(s)
    i = 0
    ans = 0
    while i+k <= len(s):
        if s[i] == '-':
            s = s[:i] + flip(s[i:i+k]) + s[i+k:]
            ans += 1
        i += 1

    print 'Case #%d:' % (_+1),
    if s.find('-') >= 0:
        print 'IMPOSSIBLE'
    else:
        print ans
