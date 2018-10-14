# Zolmeister

T = int(raw_input())

for t in xrange(T):
    N, R, O, Y, G, B, V = map(int, raw_input().split())

    stalls = []
    unicorns = sorted([
        [R, 'R'],
        [O, 'O'],
        [Y, 'Y'],
        [G, 'G'],
        [B, 'B'],
        [V, 'V']
    ])[::-1]

    is_valid = True

    for i in xrange(N):
        unicorn = unicorns[0]
        if len(stalls) > 0 and stalls[-1] == unicorn[1]:
            if unicorns[1][0] == 0:
                is_valid = False
                break
            unicorn = unicorns[1]
        stalls.append(unicorn[1])
        unicorn[0] -= 1
        unicorns = sorted(unicorns)[::-1]

    if len(stalls) > 2 and stalls[0] == stalls[-1] and stalls[-1] != stalls[-3]:
        temp = stalls[-1]
        stalls[-1] = stalls[-2]
        stalls[-2] = temp

    ans = ''.join(stalls)
    if not is_valid or ans[0] == ans[-1]:
        ans = 'IMPOSSIBLE'

    print 'Case #{}: {}'.format(t + 1, ans)
