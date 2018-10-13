def parseScalar(f,c=int):
    return c(f.next().strip('\r\n'))
def parseTuple(f,c=int):
    return tuple(c(s) for s in  f.next().strip('\r\n').split())

from collections import defaultdict
def main(fn1, fn2):
    with open(fn1) as f:
        with open(fn2, 'w') as g:
            ncases = parseScalar(f)
            for n in range(ncases):

                N, R, O, Y, G, B, V = parseTuple(f)
                print N, R, O, Y, G, B, V
                x = solveSmall(N, R, O, Y, G, B, V)
                print x

                print>>g, 'Case #%d: %s'  % (n+1,str(x))
                print 'Case #%d: %s'  % (n+1,str(x)  )



import sys, itertools
#from pulp import *
import heapq
def merge(placed,rest):
    p2 = [placed[0]]
    j=0
    for i in range(1,len(placed)):
        if j<len(rest) and placed[i-1] <> rest[j] <> placed[i]:
            p2.append(rest[j])
            j+=1
        p2.append(placed[i])
    if j<len(rest) and placed[-1] <> rest[j] :
            p2.append(rest[j])
            j+=1
    return p2,rest[j:]

def check(x,N, R, O, Y, G, B, V):
    if x[-1] == x[0]: return False
    chk = defaultdict(lambda:0)
    for i,v in enumerate(x):
        if (x[i]==x[i-1]): return False
        chk[v] += 1
    return chk['R']==R and chk['G']==G and chk['B']==B
def solveSmall(N, R, O, Y, G, B, V):
    counts =  {'B':B,'Y':Y,'R':R}
    cl = [(c,l) for (l,c) in counts.items()]
    cl.sort()
    cl.reverse()
    c,l = cl[0]
    res = l * c
    rest = ''.join(l*c for c,l in cl[1:])
    while len(res) < N:
        l = len(res)
        res,rest = merge(res,rest)
        if len(res) == l:
            return 'IMPOSSIBLE'


    if check(res,N, R, O, Y, G, B, V):
        return ''.join(res)
    else:
        return 'IMPOSSIBLE'


if __name__ == '__main__':
    main('B-test.in', 'B-test.out')
    main('B-small-attempt1.in', 'B-small-attempt1.out')
    #main('B-large.in', 'B-large.out')
    sys.exit(0)


