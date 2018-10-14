T = int(input())
for tc in range(1, T + 1):
    [N, H, L] = [int(x) for x in input().split(' ')]
    others_notes = [int(x) for x in input().split(' ')]
    res = 'NO'
    possibles = [[x, True] for x in list(range(H, L + 1))]
    for n in others_notes:
        for a, [j, f] in enumerate(possibles):
            M = max(j, n)
            m = min(j, n)
            (d, r) = divmod(M, m)
            if r != 0:
                possibles[a][1] = False
        possibles = [[x, f] for [x, f] in possibles if f == True]
        if len(possibles) == 0:
            break
    if len(possibles) != 0:
        res = min(possibles)[0]
    print('Case #{}: {}'.format(tc, res))
