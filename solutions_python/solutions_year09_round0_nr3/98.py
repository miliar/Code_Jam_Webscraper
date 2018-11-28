import os, sys

target = 'welcome to code jam'

idx = {'a': (17,), ' ': (7, 10, 15), 'c': (3, 11), 'e': (1, 6, 14),
'd': (13,), 'j': (16,), 'm': (5, 18), 'l': (2,), 'o': (4, 9, 12), 't': (8,), 'w': (0,)}

f = file('C-large.in', 'r')

def tcase():
    msg = f.readline().rstrip()
    msg = filter(lambda x: x in target, msg)
    T = [0 for i in xrange(20)]
    T[19] = 1
    for i, c in enumerate(msg[::-1]):
        for j in idx[c]:
            T[j] += T[j+1]
            T[j] %= 10000
    return T[0]

N = int(f.readline())
for i in range(1, N+1):
    print 'Case #%d: %04d' % (i, tcase())