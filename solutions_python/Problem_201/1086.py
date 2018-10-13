# Python 3
import math


def solve(N, Kprime):
    if Kprime == 0:
        return (int(math.ceil((N - 1)/2)), (N - 1)//2)
    if N%2 == 1:
        return solve(N//2, (Kprime - 1)//2)
    else:
        return solve(N//2 - int(Kprime%2 == 0), (Kprime - 1)//2)


n_cases = int(input())
for i in range(n_cases):
    N, K = [int(x) for x in input().split(' ')]
    print('Case #{}: {} {}'.format(i + 1, *solve(N, K - 1)))
