def f(n):
    n -= 1
    return (n - n // 2, n // 2)

def solve(test_num):
    n, k = map(int, input().split())
    d = dict()
    d[n] = 1
    while k > 0:
        m = max(d.keys())
        count = min(k, d[m])
        k -= count
        a, b = f(m)
        del d[m]
        d[a] = d.get(a, 0) + count
        d[b] = d.get(b, 0) + count
    ans = str(a) + " " + str(b)
    print("Case #", test_num, ": ", ans, sep="")

for i in range(1, int(input()) + 1):
    solve(i)

