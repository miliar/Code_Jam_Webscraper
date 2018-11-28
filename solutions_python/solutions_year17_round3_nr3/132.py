from math import *
from fractions import*
from heapq import*

def solve(N,K,U,P):
    heapify(P)
    while U > 0:
        prob = heappop(P)
        count = 1
        while len(P)>0 and P[0]==prob:
            count += 1
            heappop(P)

        if len(P)==0:
            prob += U/count
            ans = float(prob**count)
            if ans<0.0000001:
                ans=0
            return ans
        else:
            if U > (P[0]-prob)*count:
                U -= (P[0]-prob)*count
                prob = P[0]
                for i in range(count):
                    heappush(P,prob)
            else:
                prob += U/count
                for i in range(count):
                    heappush(P,prob)
                ans = Fraction(1)
                for i in P:
                    ans *= i
                if ans<0.0000001:
                    ans=0
                return float(ans)
    ans = Fraction(1)
    for i in P:
        ans *= i
    if ans<0.0000001:
        ans=0
    return float(ans)

f = open('C-small-1-attempt0.in','r')
g = open('output.txt','w')

T = int(f.readline())
for ind in range(T):
    # read input
    [N,K] = [int(i) for i in f.readline().split()]
    U = Fraction(f.readline())
    P = [Fraction(i) for i in f.readline().split()]

    # compute answer
    ans = solve(N,K,U,P)

    # print to file
    g.write('Case #{}: {}\n'.format(ind+1,ans))

f.close()
g.close()

