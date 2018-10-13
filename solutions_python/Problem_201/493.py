T = int(input())


memo = {}

def rec(n, k):
    if (n, k) not in memo:
        if k <= 1:
            memo[(n, k)] = ((n-1)//2, (n)//2)
        else:
            if (k-1)//2 == 0:
                memo[(n, k)] = rec((n)//2, k//2)
            else:
                memo[(n, k)] = min(rec((n-1)//2, (k-1)//2), rec(n//2, k//2))
    return memo[(n, k)]

for t in range(T):
    n, k = map(int, input().split())
    r, l = rec(n, k)
    print("Case #", t+1, ": ", max(r, l), " ", min(l, r), sep="")
