#!/usr/bin/env python

for nnn in xrange(1, int(raw_input())+1):
    print "Case #%d:" % (nnn),
    A_C, A_J = [int(x) for x in raw_input().split()]
    B_C = [[int(x) for x in raw_input().split()] for _ in xrange(A_C)]
    B_J = [[int(x) for x in raw_input().split()] for _ in xrange(A_J)]
    B_C = sorted(B_C)
    B_J = sorted(B_J)

    #small
    if A_C <= 1 and A_J <= 1:
        print 2
    elif A_J == 2:
        if B_J[0][0] + 1440-B_J[1][1] >= 720 \
              or B_J[1][0] - B_J[0][1] >= 720:
            print 2
        else:
            print 4
    elif A_C == 2:
        if B_C[0][0] + 1440-B_C[1][1] >= 720 \
              or B_C[1][0] - B_C[0][1] >= 720:
            print 2
        else:
            print 4

