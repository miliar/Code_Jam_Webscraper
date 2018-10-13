from sys import stdin
from math import *
from fractions import Fraction

def solve_D(p,N):
    for num in xrange(1,N+1):
        for wins in xrange(num+1):
            perc=wins*100.0/num
            if abs(perc-p)<1e-9:
                return True
    return False

def solve_G(pd,pg,N):
    if pd!=pg:
        if pg==0 or pg==100:
            #print "2false"
            return False
    #print "2true"
    return True

def solve_D_big(p,N):
    f=Fraction(p,100)
    return f.denominator<=N

if __name__=='__main__':
    infile=open("A.in",'r')
    outfile=open("output_big.txt","w");
    T=int(infile.readline())
    for case in xrange(1,T+1):
        N,pd,pg=map(int,infile.readline().split())
        answer=solve_D_big(pd,N) and solve_G(pd,pg,N)
        answer="Possible" if answer else "Broken"
        outfile.write("Case #%d: %s\n"%(case,answer))
    infile.close()
    outfile.close()
