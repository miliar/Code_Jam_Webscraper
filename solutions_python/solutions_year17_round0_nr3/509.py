from sortedcontainers import SortedDict

def solve(case_no):
    n, k = map(int, input().split())

    c = SortedDict()
    c[n] = 1
    k -= 1

    while k:
        t, cnt = c.popitem()
        if (t - 1) // 2 not in c:
            c[(t - 1) // 2] = 0
        if t // 2 not in c:
            c[t // 2] = 0
        c[(t - 1) // 2] += min(k, cnt)
        c[t // 2] += min(k, cnt)
        if cnt <= k:
            k -= cnt
        else:
            c[t] = cnt - k
            k = 0

    t = c.popitem()[0]
    mn, mx = (t - 1) // 2, t // 2
    print("Case #{}: {} {}".format(case_no, mx, mn))

t = int(input())
for i in range(t):
    solve(i + 1)
