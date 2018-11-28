#!/usr/bin/python

for i in xrange(input()):
    line = raw_input()
    L = line.split()
    M =int(L[0])
    S = [int(x) for x in L[1]]
    T = 0
    N = 0
    for j in range(M + 1):
        if T >= j:
            T = T + S[j]
        else:
            N = N + j - T
            T = S[j] + j
    print "Case #%d: %d" % (i+1, N)

        




