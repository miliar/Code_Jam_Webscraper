import sys
from array import array

def readInt():
	return int(sys.stdin.readline().strip())

def readInts():
	return list(map(int, sys.stdin.readline().strip().split(" ")))

def readLine():
	return list(sys.stdin.readline().strip().split(" "))

def readChars():
	return list(sys.stdin.readline().strip())

T = readInt()
for tc in xrange(T):
    N = readInt()

    A = []
    WP = []
    OWP = []
    OOWP = []
    for i in xrange(N):
        A.append(readChars())
    #print A

    for i in xrange(N):
        W = 0
        L = 0
        for j in xrange(N):
            if (A[i][j] == '1'):
                W += 1
            if (A[i][j] == '0'):
                L += 1
        WP.append([W,L])
    #print WP

    for i in xrange(N):
        s = 0
        c = 0
        for j in xrange(N):
            if (A[i][j] == '1'):
                s += (1.0 * WP[j][0]) / (WP[j][0] + WP[j][1] - 1)
                c += 1
            if (A[i][j] == '0'):
                s += (1.0 * WP[j][0]-1) / (WP[j][0] + WP[j][1] - 1)
                c += 1
        OWP.append(s/c)
    #print OWP

    for i in xrange(N):
        s = 0
        c = 0
        for j in xrange(N):
            if (A[i][j] != '.'):
                s += OWP[j]
                c += 1
        OOWP.append(s/c)
    #print OOWP

    print "Case #" + str(tc+1) + ": "
    for i in xrange(N):
        print (0.25 * (1.0 * WP[i][0] / (WP[i][0]+WP[i][1]))) + (0.50 * OWP[i]) + (0.25 * OOWP[i])

