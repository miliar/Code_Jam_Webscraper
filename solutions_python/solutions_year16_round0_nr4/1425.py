def solve(K, C, S):
    return ' '.join(map(str, range(1, K + 1)))

T = int(input())
for t in range(T):
    K, C, S = map(int, input().split())
    ans = solve(K, C, S)
    print('Case #{}: {}'.format(t + 1, ans))
