import math
def constant(n, k):
    return (n - k)//(2**int(math.log2(k)))
T = int(input())
for t in range(T):
    N, K = [int(x) for x in input().split()]
    cst = constant(N,K)
    if cst % 2 == 1:
        print('Case #{}: {} {}'.format(t + 1, math.ceil(cst/2), math.floor(cst/2)))
    else:
        print('Case #{}: {} {}'.format(t + 1, cst//2, cst//2))