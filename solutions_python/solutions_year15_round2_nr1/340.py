def parseScalar(f,c=int):
    return c(f.next().strip('\r\n'))
def parseTuple(f,c=int):
    return tuple(c(s) for s in  f.next().strip('\r\n').split())



import sys
sys.setrecursionlimit(1000)

def main(fn1, fn2):
    with open(fn1) as f:
        with open(fn2, 'w') as g:
            ncases = parseScalar(f)
            for n in range(ncases):
                N = parseScalar(f)
                print N
                x = solve(N)
                print>>g, 'Case #%d: %s'  % (n+1,x)
                print 'Case #%d: %s'  % (n+1,x  )
def revint(x):
    s = str(x)[::-1]
    return int(s)

def solve(N):
    sols = [N+2]*(N+1)
    sols[0]=0
    sols[1]=1
    for x in xrange(2,N+1):
        sols[x] = min(sols[x-1]+1, sols[x])
        rev = revint(x)
        if x < rev < N+1 :
            sols[rev] = min(sols[rev],sols[x]+1)
   # print >> open('tmp.csv','w'), '\n'.join(str(x) for x in sols)
    return sols[N]



if __name__ == '__main__':
    #solve(10400)
    #main('A-test.in', 'A-test.out')
    main('A-small-attempt0.in', 'A-small-attempt0.out')
    #main('A-large-practice.in', 'A-large-practice.out')



