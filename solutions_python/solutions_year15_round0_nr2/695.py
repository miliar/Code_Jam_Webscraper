import sys
rl = lambda: sys.stdin.readline().strip()


T = int(rl())
for tcase in range(1, T + 1):
    seen = set()
    n = int(rl())
    cakes = map(int, rl().split())
    cakes = sorted(cakes)
    Q = [(0, cakes[::])]
    answer = max(cakes)
    while len(Q) > 0:
        elapsed, cakes = Q[0]
        Q = Q[1:]
        answer = min(answer, elapsed + max(cakes))
        for i in range(len(cakes)):
            if cakes[i] == 2:
                continue
            for j in range(2, cakes[i]):
                cakes[i] -= j
                cakes.append(j)
                cand = sorted(cakes)
                if tuple(cand) not in seen:
                    seen.add(tuple(cand))
                    Q.append((elapsed + 1, cand))
                cakes.pop()
                cakes[i] += j
    print 'Case #%d: %d' % (tcase, answer)
