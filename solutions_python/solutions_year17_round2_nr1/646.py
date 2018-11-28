import math

matrix = None
NXmask = None
NPmask = None

def Solver(D,Ks,Ss):

    tmax = -1

    for k,s in zip(Ks,Ss):
        t = (D-k)/s
        if t>tmax:
            tmax = t

    return D/tmax

import sys

def main():

    with open(sys.argv[1]) as f:
        n = int(f.readline())

        for i in xrange(n):

            D,N = f.readline().strip().split()
            D,N = int(D),int(N)

            Ks,Ss = [], []

            for j in range(N):

                K,S = f.readline().strip().split()
                Ks.append(float(K))
                Ss.append(float(S))

            r = Solver(D,Ks,Ss)
            print "Case #{:d}: ".format(i+1)+str(r)
main()
