for i in range(int(raw_input())):
    N, R, O, Y, G, B, V = map(int, raw_input().split())

    if 2*max(R, Y, B) > N:
        print 'Case #{0}: IMPOSSIBLE'.format(i+1)
        continue

    unicorns = {
        'R': R,
        'O': O,
        'Y': Y,
        'G': G,
        'B': B,
        'V': V
    }

    stalls = [None for _ in range(N)]

    colors = sorted(unicorns.keys(), key=lambda c: -unicorns[c])
    m = colors[0]

    d = N - (2 * unicorns[m])
    unicorns[m] -= d
    k = d
    j = 0
    while k > 0:
        stalls[j] = m
        j += 3
        k -= 1

    while unicorns[m] > 0:
        stalls[j] = m
        j += 2
        unicorns[m] -= 1

    m = colors[1]
    unicorns[m] -= d
    k = d
    j = 1
    while k > 0:
        stalls[j] = m
        j += 3
        k -= 1

    while unicorns[m] > 0:
        stalls[j] = m
        j += 2
        unicorns[m] -= 1

    last_index = j
    m = colors[2]
    unicorns[m] -= d
    k = d
    j = 2
    while k > 0:
        stalls[j] = m
        j += 3
        k -= 1

    j = last_index
    while unicorns[m] > 0:
        stalls[j] = m
        j += 2
        unicorns[m] -= 1

    sol = ''.join(stalls)
    print 'Case #{0}: {1}'.format(i+1, sol)
