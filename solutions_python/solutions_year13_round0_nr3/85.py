# Google Code Jam 2013
# Problem C. Fair and Square
# mjacquem1

import sys
import logging
import StringIO
import math
from itertools import chain
from itertools import combinations

def echo(fn):
    def wrapped(*v, **k):
        name = fn.__name__
        logging.info( "Called %s(%s)" % (name, ", ".join(map(repr, chain(v, k.values())))) )
        res = fn(*v, **k)
        logging.info( "       %s(%s) returned %s" % (name, ", ".join(map(repr, chain(v, k.values()))),res) )
        return res
    return wrapped

def ispal(n):
    s = str(n)
    l=len(s)
    for i in xrange(l//2+1):
        if s[i]!=s[l-i-1]:
            return False
    return True

def nfs(a,b):
    res=0
    sa = int(math.sqrt(a))
    sb = int(math.sqrt(b))
    for sn in xrange(sa,sb+1):
        if ispal(sn):
            n=sn*sn
            if n>=a and n<=b and ispal(n):
                res +=1
    return res
    

def allpals(limit):
    res = set()
    for i in xrange(min(9,limit)+1):
        res.add(i)
    cont = True
    i = 1
    digs = ["","0","1","2","3","4","5","6","7","8","9"]
    while cont:
        si = str(i)
        rev = si[::-1]
        cont = False
        for d in digs:
#            print si,d,rev
            n = int(si + d + rev)
            if n<=limit:
                cont=True
                res.add(n)
        i += 1
    return res

def nfs2(a,b):
    res=0
    sa = int(math.sqrt(a))
    while sa*sa<a:
        sa +=1
    sb = int(math.sqrt(b))
    pals = allpals(sb)
    for sn in pals:
        n=sn*sn
        if n>=a and n<=b and ispal(n):
            res +=1
    return res

def nfs3(a,b):
    res=[]
    sa = int(math.sqrt(a))
    while sa*sa<a:
        sa +=1
    sb = int(math.sqrt(b))
    pals = allpals(sb)
    for sn in pals:
        n=sn*sn
        if n>=a and n<=b and ispal(n):
            res.append((sn,n))
    return sorted(res)

def allfs(n):
    "All bases of fair and square numbers <= n"
    sn = str(n)
    ln = len(sn)
    ln2 = (ln//2)+1
    s = set([1,2,3])
    for x in ["","0","1","00","01","10","11"]:
        for y in ["","0","1","2"]:
            z = int("1"+x+y+x[::-1]+"1")
            if z<=n and ispal(z*z):
                s.add(z)
    for nz in xrange(ln2):
        x = "0"*nz
        for y in ["","0","1"]:
            z = int("2"+x+y+x+"2")
            if z<=n and ispal(z*z):
                s.add(z)
    for nz in xrange(3,ln2):
        rng = range(nz)
        x = "0"*nz
        llocs = [[]] + [[i] for i in rng] + list(combinations(rng,2)) + list(combinations(rng,3))
        for locs in llocs:
            x2 = list(x)
            for loc in locs:
                x2[loc]="1"
            xx = "".join(x2)
            for y in ["","0","1","2"]:
                z = int("1"+xx+y+xx[::-1]+"1")
                if z<=n and ispal(z*z):
                    s.add(z)
    return sorted([z*z for z in s])

lallfs = allfs(10**50)

def nfs4(a,b):
    return len(filter(lambda x:x>=a and x<=b, lallfs))
    

def sp(x):
    "Smallest palindrome >= x"
    sx = str(x)
    lsx = len(sx)
    if (lsx&1)==1:
        lsx2=(lsx>>1)+1
        sx2=sx[:lsx2]
        return int(str(int(sx2)+1)+sx2[-2::-1])
    lsx2=lsx>>1
    sx2=sx[:lsx2]
    return int(str(int(sx2)+1)+sx2[::-1])

def main(data=None):
    if data is not None:
        sys.stdin = StringIO.StringIO(data)
    for tc in xrange(1, int(raw_input()) + 1):
        (a,b) = map(int,raw_input().split(' '))
        print 'Case #%d: %s' % (tc, nfs4(a,b))
    if data is not None:
        sys.stdin = sys.__stdin__

sample="""3
1 4
10 120
100 1000
"""


# Call main() only if run from command line, not from IDLE
if __name__ == "__main__":
    if True:
#    if '/' not in sys.argv[0] and '\\' not in sys.argv[0]:
        logging.basicConfig(level=logging.ERROR)
        sys.exit(main())
    else:
        logging.basicConfig(level=logging.INFO,format=" %(levelname)s: %(message)s")
