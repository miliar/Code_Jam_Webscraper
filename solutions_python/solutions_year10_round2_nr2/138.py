def solve(chickens, N, K, B, T):
    if K == 0:
        return 0

    chickens.sort()
    can_make_it = lambda x, y : x + y * T >= B
    swaps = 0
    not_made = 0
    for x, y in chickens[::-1]:
        if can_make_it(x, y):
            swaps += not_made
            K -= 1
            if K == 0:
                return swaps
        else:
            not_made += 1
    return -1


C = int(raw_input())
for c in range(1, C + 1):
    N, K, B, T = map(int, raw_input().split())
    Xs = map(int, raw_input().split())
    Ys = map(int, raw_input().split())
    chickens = zip(Xs, Ys)
    ans = solve(chickens, N, K, B, T)
    if ans == -1:
        print 'Case #%d: IMPOSSIBLE' % c
    else:
        print 'Case #%d: %d' % (c, ans)
