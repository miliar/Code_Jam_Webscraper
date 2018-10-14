def solve(n, k):
    if k == 1:
        return n//2, (n-1)//2

    if n % 2 == 0:
        if k % 2 == 0:
            return(solve(int(n/2), int(k/2)))
        if k % 2 > 0:
            return(solve(int(n/2-1), int((k-1)/2)))

    if n % 2 > 0:
        return(solve(n//2, k//2))


def solve_slower(n, k):
    s = [0, n+1]

    for i in range(k):
        max_t = 0
        max_d = 0
        for t, j in enumerate(s):
            if t == 0:
                continue

            d = j - s[t-1]
            if d == 1:
                continue

            if d > max_d:
                max_d = d
                max_t = t

        d = max_d
        t = max_t
        md = s[t-1] + d//2
        L = d//2 - 1
        R = s[t] - md - 1
        s.insert(t, md)

    return max(L, R), min(L, R), s


T = int(input())

for casenum in range(1, T+1):
    # n = int(input())
    n, k = [int(s) for s in input().split(" ")]
    # s = input()
    # print(n, k)

    x, y = solve(n, k)

    print("Case #{}: {} {}".format(casenum, x, y))
