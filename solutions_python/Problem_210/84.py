import math

HALF = 720
FULL = 1440

def solve():
    Ac, Aj = (int(x) for x in input().split())
    Ac = [tuple(int(x) for x in input().split()) for _ in range(Ac)]
    Aj = [tuple(int(x) for x in input().split()) for _ in range(Aj)]

    CJ = []
    for c, d in Ac: CJ.append((c, d, 0))
    for j, k in Aj: CJ.append((j, k, 1))
    CJ.sort()
    #print (CJ)
    res = 0
    C = [0, 0]
    P2 = [] # changes with  cost of 2
    P0 = [] # no cost
    for i in range(len(CJ)):
        a, b, cj = CJ[i]
        ap, bp, cjp = CJ[i-1]
        if i == 0:
            if cj == cjp: # no change
                C[cj] += b + FULL - bp
                P2.append((a + FULL - bp, cj))
            else: # need to change
                res += 1
                C[cj] += b + FULL - bp
                P0.append((a + FULL - bp, cj))
            continue
        if cj == cjp: # no change
            C[cj] += b - bp
            P2.append((a - bp, cj))
        else: # need to change
            res += 1
            C[cj] += b - bp
            P0.append((a - bp, cj))
    P2.sort(reverse=True)
    P0.sort(reverse=True)
    if C[0] == C[1]: return res
    need = 1 if C[0] > C[1] else 0
    needSize = abs(C[0] - C[1])
    for size, cj in P0:
        if needSize == 0 or size == 0: break
        if cj == need: continue
        needSize -= 2*size
        if needSize < 0: needSize = 0
    for size, cj in P2:
        if needSize == 0 or size == 0: break
        if cj == need: continue
        res += 2
        needSize -= 2*size
        if needSize < 0: needSize = 0
    return res

T = int(input())
for t in range(1, T + 1):
    print ("Case #%d: %d" % (t, solve()))
