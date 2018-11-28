def getN(n):
    if (n % 2 == 0):
       return (n/2-1, n/2)
    else:
       return (n/2, n/2)


def cal(n,k):
    if k == 1:
        a,b = getN(n)
        return (max(a,b),min(a,b))
    if n == 1:
        return (0,0)
    if n % 2 == 1:
        return cal((n-1)/2, k/2)
    else:
        if k % 2 == 1:
            return cal(n/2-1,k/2)
        else:
            return cal(n/2,k/2)

t = int(raw_input())

for i in range(t):
    n, k = [int(s) for s in raw_input().split(" ")]
    a, b = cal(n,k)
    print("Case #{}: {} {}".format(i+1, a, b))