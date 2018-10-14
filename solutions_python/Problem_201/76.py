from collections import defaultdict

t = int(input())

def f(n,k):
    if k == 1:
        return n-1
    k -= 1
    n -= 1

    if k%2 == 1:
        return f(n-n//2, k-k//2)
    else:
        return f(n//2, k//2)

for x in range(t):
    n,k = map(int, input().split())
    left = f(n,k)
    y,z = left-left//2, left//2
    print(f'Case #{x+1}: {y} {z}')
