from collections import Counter

def solve(testCaseNumber):
    D = int(raw_input().strip())
    P  = map(lambda x: int(x.strip()), raw_input().strip().split())
    if len(P) != D:
        raise Exception('Illegal length {0}, {1}'.format(len(P), D))
    lastMax = -1
    arrCounter = Counter()
    for n in P:
        arrCounter[n]+=1
        if lastMax < n:
            lastMax = n
    total = lastMax
    total = min(total, findMin(P))
    print 'Case #{0}: {1}'.format(testCaseNumber, total )

MEM = {}
def findMin(P):
    if len(P) == 0:
        return 0
    # interrupt:
    Q = sorted(P)
    key = tuple(Q)
    if key not in MEM:
        a = Q.pop()
        if a == 1:
            return 1
        tot = a
        for i in xrange(1, a):
            tot = min(tot, 1 + findMin(Q + [i, a-i]))
        Q = []
        for i in P:
            if i > 1:
                Q.append(i-1)
        MEM[key] = min(tot, 1+findMin(Q))
    return MEM[key]



def main():
    T = int(raw_input())
    for i in xrange(1, T+1):
        solve(i)
main()
