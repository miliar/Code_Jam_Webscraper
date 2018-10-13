import sys

sys.setrecursionlimit(1500)

def argmax(a):
    idx = 0
    for (i, e) in enumerate(a):
        if a[idx] < e:
            idx = i
    return idx

for _t in range(1, int(raw_input())+1):
    D = int(raw_input())
    P = map(int, raw_input().strip().split())
    def dfs():
        global P
        eatResult = max(P)

        moveResult = float("inf")
        biggestIdx = argmax(P)
        for nmove in range(2, P[biggestIdx] // 2 + 1):
            P[biggestIdx] -= nmove
            P.append(nmove)
            moveResult = min(moveResult, 1+dfs())
            P.pop()
            P[biggestIdx] += nmove

        return min(eatResult, moveResult)
    print "Case #%d: %d" % (_t, dfs())
