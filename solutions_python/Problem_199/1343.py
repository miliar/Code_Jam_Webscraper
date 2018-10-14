import sys

def flip(S,K):
    lS = len(S)
    fcount =0
    for i in xrange(lS):
        if S[i] == '+':
            continue
        if i>lS-K:
            return "IMPOSSIBLE"
        fcount+=1
        for j in xrange(i,i+K):
            S[j] = '+' if S[j]=='-' else '-'

    return str(fcount)

#fp = open('test.in')
fp=sys.stdin
T=int(fp.readline())

for t in xrange(T):
    S,Ks = fp.readline().split()
    K = int(Ks)
    S = list(S)

    print "Case #%d: %s"%(t+1,flip(S,K))