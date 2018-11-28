# python 3
import math
t = int(input())
def solve(n,k):
    stalls = "0" * n
    ls=rs=0
    for i in range(k):
        cnd = sorted(stalls.split("1"), key=lambda x:-len(x))[0]
        idx =math.floor((len(cnd) - 1)/2) 
        rep = cnd[:idx] + "1" + cnd[idx+1:]
        ls,rs = len(cnd[:idx]), len(cnd[idx+1:])
        stalls = stalls.replace(cnd, rep, 1)
    return (stalls, ls, rs)

for i in range(t):
    n,k = [int(x) for x in input().split(" ")]
    res = solve(n, k)
    print("Case #" + str(i+1) + ": " + str(max(res[1],res[2])) + " " + str(min(res[1],res[2])))
