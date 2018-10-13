def solve_one(d, k, s):
    t = (d - k) / s
    return d / t


def solve(d, n, k, s):
    ans = 1e100
    for i in range(0, n):
        maxans = solve_one(d, k[i], s[i])
        if maxans < ans:
            ans = maxans
    return ans

T = int(input())

for case in range(1,T+1):
    d,n=tuple(map(int,list(input().split())))
    k=[]
    s=[]
    for i in range(0, n):
        ki,si=tuple(map(int, list(input().split())))
        k.append(ki)
        s.append(si)
    a = solve(d, n, k, s)
    print("Case #{}: {:.8f}".format(case, a))