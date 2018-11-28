from math import *;
import fractions
import sys

def solve(v):
    v.sort()
    d=[]
    for i in range(1,len(v)):
        d.append(v[i]-v[i-1])  
    #print d
    gcd=d[0]
    for i in range(1,len(d)):
        gcd=fractions.gcd(gcd,d[i])
    return (gcd-(v[0]%gcd))%gcd
if __name__== '__main__':
    cases=  int( sys.stdin.readline())
    for i in range(cases):
        v=[ int(item) for item in sys.stdin.readline().split() ]
        print 'Case #%d: %d'%(i+1,solve(v[1:]))