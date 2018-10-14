def solve(N, m):
    ans1 = 0
    for i in range(N-1):
        ans1 += max(0, m[i]-m[i+1])

    ans2 = 0
    rate = 0
    for i in range(N-1):
        rate = max(rate, m[i]-m[i+1])
    for i in range(N-1):
        ans2 += min(rate, m[i])

    return (ans1, ans2)

for t in range(input()):
    N = input()
    m = map(int, raw_input().split())
    ans = solve(N, m)
    print "Case #%s: %s %s"%(t+1, ans[0], ans[1])
