#!/usr/bin/python

for ii in xrange(input()):
    D = input()
    line = raw_input()
    P = map(int, line.split())
    P.sort()
    i = 0
    T = [P[-1] + 0];

    while P[-1] > 3:
        i = i + 1 
        if P[-1] == 9 and ((D > 1 and max(P[0:-1]) in [1, 2, 3, 6]) or D == 1):
            P[-1] = 3
            P.append(6)
            P.sort()
            T.append(P[-1] + i)
        else:
            A = P[-1] / 2
            B = P[-1] - A
            P[-1] = A
            P.append(B)
            P.sort()
            T.append(P[-1] + i)
    
    print "Case #%d: %d" % (ii+1, min(T))
