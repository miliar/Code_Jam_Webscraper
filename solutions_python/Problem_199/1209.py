def parseScalar(f,c=int):
    return c(f.next().strip('\r\n'))
def parseTuple(f,c=int):
    return tuple(c(s) for s in  f.next().strip('\r\n').split())


def main(fn1, fn2):
    with open(fn1) as f:
        with open(fn2, 'w') as g:
            ncases = parseScalar(f)
            for n in range(ncases):
                S,K = parseTuple(f,str)
                K = int(K)
                pan = [c=='+' for c in S]

                x = solve(S,K)
                print>>g, 'Case #%d: %s'  % (n+1,str(x))
                print 'Case #%d: %s'  % (n+1,str(x)  )


import sys, itertools

def flip(S,i,K):
    for j in range(i,i+K):
        if S[j]=='+':
            S[j] = '-'
        else:
            assert S[j] == '-'
            S[j] = '+'

def solve(S,K):
    S = list(S)
    c = 0
    print ''.join(S)
    for i in range(len(S)-K+1):
        if S[i] == '-':
            flip(S,i,K)
            c += 1
            print ''.join(S)
    for i in range(len(S)-K,len(S)):
        if S[i] == '-':
            return 'IMPOSSIBLE'
    return str(c)

if __name__ == '__main__':
    #main('A-test.in', 'A-test.out')
    #main('A-small-attempt0.in', 'A-small-attempt0.out')
    main('A-large.in', 'A-large.out')
    sys.exit(0)


