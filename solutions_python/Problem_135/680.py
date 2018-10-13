__author__ = 'Alen'

import sys

N = int(sys.stdin.readline().strip())
for qw in range(1, N+1):
    print 'Case #%d:' % qw,

    l1 = int(sys.stdin.readline().strip())
    n1 = []
    for i in range(4):
        s = sys.stdin.readline().strip()
        if i == l1 - 1:
            n1 = s.split(' ')

    l2 = int(sys.stdin.readline().strip())
    n2 = []
    for i in range(4):
        s = sys.stdin.readline().strip()
        if i == l2 - 1:
            n2 = s.split(' ')

    ne = 0
    thenum = 0
    for n in n2:
        try:
            n1.index(n)
            ne += 1
            thenum = n
        except ValueError:
            pass
    if ne == 0:
        print 'Volunteer cheated!'
    elif ne == 1:
        print thenum
    else:
        print 'Bad magician!'