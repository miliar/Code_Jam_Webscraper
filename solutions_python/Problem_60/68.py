C = int(raw_input())
for c in range(C):
    [N, K, B, T] = map(int, raw_input().split(' '))
    X = reversed(map(int, raw_input().split(' ')))
    V = reversed(map(int, raw_input().split(' ')))
    stuck = 0
    swaps = 0
    arrived = 0
    for Xi, Vi in zip(X, V):
        t_arr = float(B-Xi)/Vi
        if t_arr > T:
            stuck += 1
        else:
            arrived += 1
            swaps += stuck
        if arrived >= K:
            break
    if arrived < K:
        swaps = 'IMPOSSIBLE'
    print 'Case #%d: %s' % (c+1, swaps)

            


    