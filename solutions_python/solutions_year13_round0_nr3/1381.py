'''
Created on Apr 13, 2013
@author: jean
'''
import math

TRUE = set([True,])
_DEBUG=False

def palin(n):
    s=str(n)
    l=len(s)
    c=l-1
    l=int(l/2)
    
    if c>0:
        #print n,s,l,c
        for i in xrange(l):
            if s[i]!=s[c]: 
                return False
            c -= 1
    
    return True

def game(x,y):
    if _DEBUG: print x,y
    ret=0
    m=y+1
    for n in xrange(x,m):
        if palin(n):
            r = int(math.sqrt(n)) 
            if r*r == n:
                if palin(r):
                    ret += 1
                
    return ret


def main(inp,outp):
    N = int(inp.readline())
    for i in xrange(N):
        if _DEBUG: print "==================", i+1
        str = inp.readline().strip()
        sx,sy = str.split()
        x=int(sx)
        y=int(sy)
        res = game(x,y)
        outp.write ("Case #%d: %s\n" % (i + 1, res))
        if _DEBUG: print "***************",res
        if _DEBUG: print

if __name__ == '__main__':
    import sys
    #main(sys.stdin,sys.stdout)
    #inf=open("C.in","rU")
    #ouf=open("C.out","w")
    inf=open("C-small-attempt0.in","rU")
    ouf=open("C-small-attempt0.out","w")
    #inf=open("C-large.in","rU")
    #ouf=open("C-large.out","w")
    main(inf,ouf)
    #_DEBUG=False
    #for i in 1000: main(inf,ouf)
    inf.close()
    ouf.close()

            