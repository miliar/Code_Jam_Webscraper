import sys
inp = sys.stdin.readlines()

cases = int(inp.pop(0))

for case in range(1, cases + 1):
    N, P = map(int, inp.pop(0).strip().split())
    R = map(int, inp.pop(0).strip().split())
    Q = [map(int, inp.pop(0).strip().split()) for _ in range(N)]

    matched = []
    for n in range(N):
        made = []
        for p in range(P):
            max_made = Q[n][p] * 100 / (R[n] * 90)
            min_made = -(Q[n][p] * 100 / -(R[n] * 110))
            if max_made < min_made:
                continue
            made.append((min_made, max_made))
        made.sort(key=lambda (a,b): -a * 1000000 - b)
        matched.append(made)

    found = 0
    done = False
    while not done:
        max_found = 0
        for n in range(N):
            if not matched[n]:
                done = True
                break
            if matched[n][-1][0] > max_found:
                max_found = matched[n][-1][0]
        if done:
            break
        bad = False
        for n in range(N):
            if matched[n][-1][1] < max_found:
                matched[n].pop()
                bad = True
        if not bad:
            for n in range(N):
                matched[n].pop()
            found += 1

    result = found
    print 'Case #{}: {}'.format(case, result)
