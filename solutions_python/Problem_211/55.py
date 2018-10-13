t = int(input())
for ti in range(1, t + 1):
    data = [int(k) for k in input().split(' ')]
    n = data[0]
    u = float(input())
    p = sorted([float(k) for k in input().split(' ')])
    for ni in range(n-1, -1, -1):
        diff = 0.0
        for nj in range(0, ni):
            diff += p[ni] - p[nj]
        if diff <= u:
            u -= diff
            for nj in range(0, ni + 1):
                p[nj] = p[ni] + u / (ni + 1)
            break
    ans = 1
    for pi in p:
        ans *= pi
    print('Case #{}: {}'.format(ti, ans))
