import sys
import fileinput
from fractions import gcd

i=0
R,k,N=0,0,0
for line in fileinput.input():
    if i>0:
        if i%2 == 1:
            R, k, N = line.split(' ')
            R=int(R)
            k=int(k)
            N=int(N)
        if i%2 == 0:
            g = line.split(' ')
            g = [int(x) for x in g]
            t = [[] for x in g]
            for p in xrange(len(g)):
                sum = g[p]
                pos = p
                while sum <= k:
                    pos = (pos+1)%len(g)
                    if sum + g[pos] > k or pos==p:
                        t[p] = [(sum, pos)]
                        sum += k
                    sum += g[pos]
            #print 't: ', t
            for q in xrange(1,28):
                for p in xrange(len(g)):
                    np = t[p][q-1][1]
                    t[p] += [(t[p][q-1][0] + t[np][q-1][0], t[np][q-1][1])]
            np = 0
            ret = 0
            q=0
            while R>0:
                if R%2==1:
                    ret += t[np][q][0]
                    np = t[np][q][1]
                R /= 2
                q +=1
            print 'Case #%d: %d' % (i/2, ret)

    i+=1



