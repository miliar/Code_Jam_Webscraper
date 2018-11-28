#!/usr/bin/python

tests = input()

for test in range(tests):
    m, n = map(int, raw_input().split())
    matr = [map( int, ''.join(bin(car)[2:].zfill(4) for car in map(lambda x: int(x, 16), raw_input().strip())) ) for i in range(m)]

    Pa = [ [0]*(n+1) for i in range(m+1) ]
    Pb = [ [0]*(n+1) for i in range(m+1) ]

    mlen = min(n, m)
    Mlen = [ [min(i,j) for j in range(n+1)] for i in range(m+1) ]
    remain = m*n

    cuts = {}

    def calcP(P, matr, value):
        for i in range(1,m+1):
            for j in range(1,n+1):
                P[i][j] = (P[i-1][j]) + (P[i][j-1]) - (P[i-1][j-1]) + ( matr[i-1][j-1] == 1 and ((i+j)&1) == value )

    calcP(Pa, matr, 1)
    calcP(Pb, matr, 0)

    def doTest(Pa, Pb, Mlen, matr):
        mlen_achieved = 0
        coord = None
        for i in range(1,m+1):
            for j in range(1, n+1):
                # am dat de gaurica?
                for length in reversed(xrange(1, min(Mlen[i][j], mlen)+1)):
                    # works?
                    nsqra = Pa[i][j] - Pa[i-length][j] - Pa[i][j-length] + Pa[i-length][j-length]
                    nsqrb = Pb[i][j] - Pb[i-length][j] - Pb[i][j-length] + Pb[i-length][j-length]
                    if ((nsqra == length*length/2 + ((length&1) and ((i+j)&1) == 1)) and nsqrb == 0) or \
                       ((nsqrb == length*length/2 + ((length&1) and ((i+j)&1) == 0)) and nsqra == 0):
                        if length > mlen_achieved:
                            mlen_achieved = length
                            coord = (i, j, length)
                        if length == mlen:
                            return coord
                        break
        return coord

    while remain and mlen > 1:
        coord = doTest(Pa, Pb, Mlen, matr)
        #print coord
        # cut it out
        if coord:
            cuts[coord[2]] = cuts.get(coord[2], 0) + 1
            remain -= coord[2]*coord[2]
            mlen = coord[2]
            # update the maximum length available from each square
            for i in range(coord[0]-coord[2]+1, m+1):
                for j in range(1, n+1):
                    if coord[0]-coord[2]+1 <= i <= coord[0] and \
                        coord[1]-coord[2]+1 <= j <= coord[1]:
                        Mlen[i][j] = 0
                    else:
                        Mlen[i][j] = Mlen[i][j] and (min(Mlen[i-1][j]+1, Mlen[i][j-1]+1, Mlen[i-1][j-1]+1)) or 0
        else:
            # IMPOSSIBLE?
            break

    cuts[1] = cuts.get(1, 0) + (mlen == 1 and remain)
    if 1 in cuts and not cuts[1]:
        del cuts[1]
    rez = len(cuts.keys())
    print 'Case #{0}: {1}'.format(test+1, rez)
    for i, j in sorted(cuts.items(), reverse=True):
        print i, j
