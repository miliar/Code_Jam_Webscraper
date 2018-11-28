import sys

class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}
    def __call__(self, *args):
        if not self.memo.has_key(args):
            self.memo[args] = self.fn(*args)
        return self.memo[args]

@Memoize
def bf(P,start,A):
    """P per pack, A contains counts modulo P"""
    bonus = 0 if start else 1
    best = 0
    for i in range(1,P):
        if A[i]==0:
            continue
        A2=list(A)
        A2[i]-=1
        best=max(best,bonus+bf(P,(start+i)%P,tuple(A2)))
    return best

def go():
    N,P = map(int,raw_input().split())
    G = map(int,raw_input().split())
    M=[0]*P
    t = 0
    for g in G:
        M[g%P]+=1
    t += M[0]
    M[0] = 0
    return t + bf(P,0,tuple(M))
    
    D,N = M.split()
    D = int(D)
    N = int(N)
    A = []
    for i in range(N):
        K,S = raw_input().split()
        K=int(K)
        S=int(S)
        # Compute time to reach end
        A.append(float(D-K)/S)
    t = max(A)
    return D/t

#sys.stdin=open('dataa.txt')

for p in range(2,5):
    for start in range(p):
        for a in range(101):
            for b in range(101):
                for c in range(101):
                    bf(p,start,(0,a,b,c))
T=input()
for t in range(1,T+1):
    print "Case #{}: {}".format(t,go())

