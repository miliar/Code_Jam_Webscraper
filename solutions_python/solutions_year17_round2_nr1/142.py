
def solve():
    D, N = [int(x) for x in input().strip().split()]
    t = 0
    for i in range(N):
        K, S = [int(x) for x in input().strip().split()]
        t = max( (D - K)/S, t)
    return D/t

t = int(input())
for i in range(t):
    ans = solve()
    print("Case #%d: %f" %(i+1, ans))
