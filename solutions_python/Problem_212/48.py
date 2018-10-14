import sys

def getWords():
    return sys.stdin.readline().strip().split()

def getInts():
    return [int(i) for i in getWords()]

def getInt():
	i = getInts()
	assert len(i)==1
	return i[0]

#sys.stdin = open('A.in')

def ct(G,P):
    r = [0]*P
    for g in G:
        r[g%P] += 1
    return tuple(r)

def compute(G, P):
    r = ct(G,P)
    res = r[0]
    if P==2:
        res += (r[1]+1)//2
    elif P==3:
        res += min(r[1],r[2]) + (abs(r[1]-r[2]) + 2)//3
    elif P==4:
        res += min(r[1], r[3])
        odd = abs(r[1] - r[3])
        res += r[2]//2
        even = r[2]%2
        if even==1 and odd >=2:
            res += 1
            even -= 1; odd -= 2
        res += odd//4
        odd %= 4
        res += (even+odd>0)
    else:
        assert False
    return res

# testing - since small test case doesn't cover P==4. argh
'''from itertools import product
for P in range(2,5):
    for N in xrange(2,11):
        bad = False
        print P, N
        sys.stdout.flush()
        D = dict()
        D2 = dict()
        for G in product(range(P), repeat=N):
            t = ct(G,P)
            if t not in D:
                D[t] = compute(G, P)
                assert t not in D2
                D2[t] = 0

            r2 = 0
            s = 0
            for g in G:
                r2+=(s==0)
                s += g
                if s>=P: s-=P

            D2[t] = max(D2[t],r2)
                    
            if D[t] < r2:
                print '! ', list(G), D[t], r2

        for t in D:
            if D[t] > D2[t]:
                print '# ', t, D[t], D2[t]'''

T = getInt()
for caseNo in xrange(1,T+1):
    N, P = getInts()
    G = getInts()
    
    print "Case #%d: %d"%(caseNo, compute(G,P))

