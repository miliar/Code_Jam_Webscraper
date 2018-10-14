import sys

from collections import defaultdict

def do():
    S = input().split()
    n = int(S[0])
    C = [int(x) for x in S[1:]]
    
    # R O Y G B V
    # 0 1 2 3 4 5
    
    cols = 'ROYGBV'
    bob = rgr = yvy = 0
    
    # O -> BOB
    if C[1] > 0:
        C[4] -= C[1]
        bob = C[1]

    # G -> RGR
    if C[3] > 0:
        C[0] -= C[3]
        rgr = C[3]

    # V -> YVY
    if C[5] > 0:
        C[2] -= C[5]
        yvy = C[5]

    C = [C[0], C[2], C[4]]
    n = sum(C)

    possible = C[0] + C[1] >= C[2] and \
               C[1] + C[2] >= C[0] and \
               C[2] + C[0] >= C[1] or n == 1

    if possible:
        sol = [None]*n

        me,mi = max((e,i) for i,e in enumerate(C))
        i = 0
        while C[mi] > 0:
            sol[i] = mi
            C[mi] -= 1
            i += 2

        me,mi = max((e,i) for i,e in enumerate(C))
        i = n-1 if (n-1)%2 else n-2
        while C[mi] > 0:
            sol[i] = mi
            C[mi] -= 1
            i -= 2

        me,mi = max((e,i) for i,e in enumerate(C))
        for i in range(n):
            if sol[i] == None:
                sol[i] = mi
                C[mi] -= 1
        #print(sol)

        res = ''
        for s in sol:
            if s == 0:
                res += 'RG'*rgr + 'R'
                rgr = 0
            elif s == 1:
                res += 'YV'*yvy + 'Y'
                yvy = 0
            elif s == 2:
                res += 'BO'*bob + 'B'
                bob = 0
        if rgr > 0:
            res += rgr*'RG'
        if yvy > 0:
            res += yvy*'YV'
        if bob > 0:
            res += bob*'BO'
        
        #print(''.join(cols[x] for x in sol))
        return res
    else:
        return 'IMPOSSIBLE'

t = int(input())

for _ in range(t):
    print(f'Case #{_+1}: {do()}')
    

