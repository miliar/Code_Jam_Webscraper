def solve(d,n,ks):

    return d/max(ks)


_T = int(input())
for _i in range(1, _T + 1):

    d,n = map(int,input().split(" "))

    ks = []
    for i in range(n):
        k,s = map(int,input().split(" "))
        ks.append((d-k)/s)

    print("Case #%d: %f" % (_i, solve(d,n,ks)))

