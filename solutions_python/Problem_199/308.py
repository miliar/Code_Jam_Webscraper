#p1

def solve(S, K):
    A = map(lambda x: +(x == '+'), S)
    N = len(A)
    ans = 0
    for i in xrange(N - K + 1):
        if not A[i]:
            ans += 1
            for j in xrange(i, i + K):
                A[j] ^= 1
    return ans if all(A) else "IMPOSSIBLE"


######
fo = open('out.txt','w')
with open('in.txt','r') as fi:
    rr = lambda: fi.readline().strip()
    rrI = lambda: int(rr())
    rrM = lambda: map(int,rr().split())
    for tc in xrange(rrI()):
        S, K = rr().split()
        K = int(K)
        zetaans = solve(S, K)
        zeta = "Case #%i: "%(tc+1) + str(zetaans)
        print zeta
        fo.write(zeta+'\n')
fo.close()
