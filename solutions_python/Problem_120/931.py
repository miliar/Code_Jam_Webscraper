'''
Created on Apr 26, 2013
@author: jean
'''
import math

_DEBUG=True


def game(r,t,nf=None):
    if _DEBUG: print r,t
    cur = r
    left = t
    n = 1
    cur1 = cur + 1
    surf =  cur1 * cur1 -  cur * cur 
    left -= surf 
    if left < 0: return 1
    while True:
        surf += 4
        left -= surf
        if nf: nf.write ("%d|%d|%d\n" %  (n,left,surf))
        if left < 0: break
        n += 1
    return str(n)

def main(inp,outp):
    N = int(inp.readline())
    for i in xrange(N):
        #if _DEBUG: print "==========================================", i+1
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
    #inf=open("A1A.in","rU")
    #ouf=open("A.out","w")
    inf=open("A-small-attempt0.in","rU")
    ouf=open("A-small-attempt0.out","w")
    #inf=open("A-large.in","rU")
    #ouf=open("A-large.out","w")
    main(inf,ouf)
    #nf=open("A1A.n","w")
    #game(1, 1000000000000000000, nf)
    #nf.close()
    inf.close()
    ouf.close()

            