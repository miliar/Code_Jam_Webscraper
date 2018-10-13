t = int(input())

from functools import lru_cache

def best(idx, hrs):
    if idx == end:
        return 0
    if (idx, hrs) in memo:
        return memo[idx, hrs]

    jdx, dist = fwd[idx]

    opt1 = float("inf")
    if hrs != -1 and e[hrs] >= totdist[jdx] - totdist[hrs]:
        opt1 = dist / s[hrs] + best(jdx, hrs)
    opt2 = float("inf")
    if e[idx] >= totdist[jdx] - totdist[idx]:
        opt2 = dist / s[idx] + best(jdx, idx)
    memo[idx,hrs] = min(opt1, opt2)
    return min(opt1, opt2)

for q in range(t):
    n, _ = map(int, input().split())
    e = [0]*n
    s = [0]*n
    for i in range(n):
        e[i], s[i] = map(int, input().split())
    fwd = [-1 for i in range(n)]
    for i in range(n):
        p = list(map(int, input().split()))
        for j in range(n):
            if p[j] != -1:
                fwd[i] = (j, p[j])

    st, end = map(int, input().split())
    st -= 1
    end -= 1
    totdist = [0]*n
    i = st
    while fwd[i] != -1:
        j, d = fwd[i]
        totdist[j] = totdist[i] + d
        i = j

    memo = {}
    res = best(st, -1)
    print("Case #{}: {:.6f}".format(q+1, res))
