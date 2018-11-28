for tc in range(int(input())):
    X, R, C = map(int, input().split())

    print('Case #{}: {}'.format(tc + 1, 'RICHARD' if X > 6 or (R * C) % X != 0 or (min(R, C) == 1 and X > 2) or (min(R, C) > 1 and X > min(R, C) * 2 - 1) else 'GABRIEL'))
