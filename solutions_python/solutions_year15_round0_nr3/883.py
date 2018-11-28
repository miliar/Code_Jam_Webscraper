__author__ = 'sanjay'

import sys

dt = {('1', 'i'): 'i', ('1', 'j'): 'j', ('1', 'k'): 'k', ('1', '1'): '1',
    ('i', '1'): 'i', ('i', 'i'): '-1', ('i', 'j'): 'k', ('i', 'k'): '-j',
    ('j', '1'): 'j', ('j', 'i'): '-k', ('j', 'j'): '-1', ('j', 'k'): 'i',
    ('k', '1'): 'k', ('k', 'i'): 'j', ('k', 'j'): '-i', ('k', 'k'): '-1',
    ('-1', 'i'): '-i', ('-1', 'j'): '-j', ('-1', 'k'): '-k', ('-1', '1'): '-1',
    ('-i', '1'): '-i', ('-i', 'i'): '1', ('-i', 'j'): '-k', ('-i', 'k'): 'j',
    ('-j', '1'): '-j', ('-j', 'i'): 'k', ('-j', 'j'): '1', ('-j', 'k'): '-i',
    ('-k', '1'): '-k', ('-k', 'i'): '-j', ('-k', 'j'): 'i', ('-k', 'k'): '1'}


def yn(s):
    temp = '1'
    i = 0
    fi, fj, fk = False, False, False
    while i < len(s):
        temp = dt[(temp, s[i])]
        if temp == 'i':
            fi = True
            break
        i += 1
    if i < len(s):
        i += 1
        temp = '1'
        while i < len(s):
            temp = dt[(temp, s[i])]
            if temp == 'j':
                fj = True
                break
            i += 1
    if i < len(s):
        temp = '1'
        for j in range(i + 1, len(s)):
            temp = dt[(temp, s[j])]
    if temp == 'k':
        fk = True
    if fi and fj and fk:
        return 'YES'
    else:
        return 'NO'

test = int(input())

for i in range(test):
    l, x = map(int, sys.stdin.readline().split())

    s = str(sys.stdin.readline()).strip() * x

    print 'Case #%d: %s' % (i + 1, yn(s))