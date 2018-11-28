def parseScalar(f,c=int):
    return c(f.next().strip('\r\n'))
def parseTuple(f,c=int):
    return tuple(c(s) for s in  f.next().strip('\r\n').split())


def main(fn1, fn2):
    with open(fn1) as f:
        with open(fn2, 'w') as g:
            ncases = parseScalar(f)
            for n in range(ncases):
                N,K = parseTuple(f)
                print N,K
                stack = []
                for i in range(N):
                    Ri,Hi = parseTuple(f, float)
                    stack.append((Ri,Hi))
                x = solve(K,stack)
                print>>g, 'Case #%d: %s'  % (n+1,str(x))
                print 'Case #%d: %s'  % (n+1,str(x)  )


import sys, itertools,math
def solve(K,stack):
    best = -1
    heights = [2*ri*hi for (ri,hi) in stack]
    base = [ri**2 for (ri,hi) in stack]
    bh = zip(base,heights)
    bh.sort(reverse=True)
    for i in range(len(bh)):
        bs = bh[i][0]+bh[i][1] # base+height of first pancake
        hh = [h for (b,h) in bh[i+1:]]
        if len(hh) < K-1:
            break
        hh.sort(reverse = True)
        s = bs + sum(hh[:K-1])
        if s > best:
            best = s
    return best*math.pi




if __name__ == '__main__':
    #main('A-test.in', 'A-test.out')
    #main('A-small-attempt0.in', 'A-small-attempt0.out')
    main('A-large.in', 'A-large.out')
    sys.exit(0)


