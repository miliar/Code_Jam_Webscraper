num_cases = int(input())

for c in range(num_cases):
    D, N = map(int, input().split())
    max_t = 0
    for i in range(N):
        Ki, Si = map(int, input().split())
        max_t = max(max_t, (D - Ki) / Si)

    r = D / max_t
    print('Case #{}: {}'.format(c + 1, r))
