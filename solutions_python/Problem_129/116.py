# Google Code Jam 2013 Round 2
# Problem A. Ticket swapping
# MichelJ

import sys
import logging
import StringIO
from itertools import chain

def echo(fn):
    def wrapped(*v, **k):
        name = fn.__name__
        logging.info( "Called %s(%s)" % (name, ", ".join(map(repr, chain(v, k.values())))) )
        res = fn(*v, **k)
        logging.info( "       %s(%s) returned %s" % (name, ", ".join(map(repr, chain(v, k.values()))),res) )
        return res
    return wrapped

def cost(delta,N):
    return (N*(N+1)-(N-delta)*(N-delta+1))//2

def ticket(N,M,o,e,p):
    transit=(N-1)*[0]
    fullcost = sum(cost(e[i]-o[i],N)*p[i] for i in xrange(M))
    for i in xrange(M):
        pi = p[i]
        for s in xrange(o[i],e[i]):
            transit[s] += pi
    bestcost=0
    inito=0
    while True:
        o = inito
        while o<N-1 and transit[o]==0:
            o += 1
        if o==N-1:
            break
        inito = o
        l=0
        while o<N-1 and transit[o]>0:
            l+=1
            transit[o] -= 1
            o+=1
        bestcost += cost(l,N)
    return fullcost-bestcost
    

def main(data=None):
    if data is not None:
        sys.stdin = StringIO.StringIO(data)
    for tc in xrange(1, int(raw_input()) + 1):
        (N,M) = map(int,raw_input().split(' '))
        o = M*[None]
        e = M*[None]
        p = M*[None]
        for i in xrange(M):
            (oi,ei,p[i]) = map(int,raw_input().split(' '))
            o[i]=oi-1
            e[i]=ei-1
        print 'Case #%d: %s' % (tc, ticket(N,M,o,e,p))
    if data is not None:
        sys.stdin = sys.__stdin__

sample="""3
6 2
1 3 1
3 6 1
6 2
1 3 2
4 6 1
10 2
1 7 2
6 9 1
"""


# Call main() only if run from command line, not from IDLE
if __name__ == "__main__":
    if True:
#    if '/' not in sys.argv[0] and '\\' not in sys.argv[0]:
        logging.basicConfig(level=logging.ERROR)
        sys.exit(main())
    else:
        logging.basicConfig(level=logging.INFO,format=" %(levelname)s: %(message)s")
