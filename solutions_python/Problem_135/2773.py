#!/usr/bin/env python

def calc(a1, b1, a2, b2):
    c1 = set(b1[a1 - 1])
    c2 = set(b2[a2 - 1])
    c = c1 & c2
    if len(c) == 1:
        return c.pop()
    elif len(c) > 0:
        return 'Bad magician!'
    else:
        return 'Volunteer cheated!'

T = input()
for t in xrange(T):
    a1 = input()
    b1 = [[int(j) for j in raw_input().split()] for i in xrange(4)]
    a2 = input()
    b2 = [[int(j) for j in raw_input().split()] for i in xrange(4)]
    print('Case #{}: {}'.format(t + 1, calc(a1, b1, a2, b2)))
