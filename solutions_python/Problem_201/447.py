from collections import Counter

def solve(N, K):
    spaces = Counter([N])
    while K > 0:
        size = max(spaces)
        number = spaces.pop(size)
        K -= number
        L = (size - 1) // 2
        R = size // 2
        if L: spaces[L] += number
        if R: spaces[R] += number
    return R, L

T = int(input())
for x in range(1, T + 1):
    N, K = map(int, input().split())
    print('Case #{}: {} {}'.format(x, *solve(N, K)))
