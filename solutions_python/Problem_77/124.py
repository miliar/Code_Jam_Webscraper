from sys import argv
from itertools import izip, imap, count, combinations, permutations
import math

maxi = 2**128
eroot = 1.0 / math.exp(1)

class rk_proto:
    def __init__(self):
        self.rk = [1, 0, 1, 2, 9]
    def __call__(self, n):
        try:
            return self.rk[n]
        except IndexError:
            m = len(self.rk)
            for i in xrange( m, n+1 ):
                self.rk.append( i * self.rk[i-1] - ((i&1)<<1) + 1 ) #( -1 if i%2 else 1 ) , - (i%2)*2 + 1 , - (i&1)*2 + 1
            return self.rk[n]

class factorial_proto:
    def __init__(self):
        self.fac = [1, 1, 2, 6, 24, 120]
    def __call__(self, n):
        try:
            return self.fac[n]
        except IndexError:
            m = len(self.fac)
            for i in xrange( m, n+1 ):
                faci = i * self.fac[i-1]
                if faci > maxi:
                    faci = float(faci)
                self.fac.append( faci )
            return self.fac[n]

rk, fac = rk_proto(), factorial_proto()

def pnk(n, k):
    if k > 12:
        return eroot / fac(n-k)
    else :
        return ( float(rk(k)) / fac(k) ) / fac(n-k)

class e_proto:
    def __init__(self):
        self.e = [ 0.0, 0.0, 2.0 ]
    def __call__(self, n):
        try:
            return self.e[n]
        except IndexError:
            m = len(self.e)
            for i in xrange( m, n+1 ):
                psk = 0.0
                for e, j in izip( self.e[2:i], count(2) ):
                    #print e, j
                    psk += e * pnk(i, j)
                ei = (psk + 1) / (1 - pnk(i,i))
                #print i, psk, pnk(i,i), ei
                self.e.append( ei )
            return self.e[n]

e = e_proto()
e(3)

def same( per ):
    copy = [ i for i in per ]
    copy.sort()
    ret = 0
    for i,j  in izip(copy, per):
        if i==j:
             ret += 1
    return ret

def solvecase( line ):
    line = line.split()
    line = map( int, line )
    n = len(line) - same( line )
    return e(n)

def main():
    global inf
    inf = argv[1]
    inf = open(argv[1])
    ncase = int(inf.readline().strip())
    for case in xrange(1, ncase+1):
        l = inf.readline().strip()
        l = inf.readline().strip()
        ans = solvecase( l )
        print "Case #{n}: {ans:.6f}".format(n=case, ans=float(ans))

main()








