t = int(input())
for case in range(1, t + 1):
    D, N = [int(part) for part in input().split(' ')]
    T = []
    for horse in range(N):
        K, S = [int(part) for part in input().split(' ')]
        T.append((D - K) / S)
    print('Case #{}: {}'.format(case, D / max(T)))
