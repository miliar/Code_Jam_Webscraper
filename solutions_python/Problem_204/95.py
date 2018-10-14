#!/usr/bin/env python3


T = int(input())
for t in range(T):
    N, P = map(int, input().split())
    R = map(int, input().split())
    I = [[] for _ in range(N)]
    points = set()
    for Is, q in zip(I, R):
        Qs = map(int, input().split())
        for Q in Qs:
            Q *= 10
            l = (Q + 11 * q - 1) // (11 * q)
            r = Q // (9 * q)
            if l <= r:
                Is.append((l, r))
                points.add(l)
                points.add(r)
    ans = 0
    for p in sorted(points):
        flag = True
        while flag:
            for Is in I:
                if not any(l <= p <= r for (l, r) in Is):
                    flag = False
                    break
            if flag:
                ans += 1
                for Is in I:
                    minr = 10 ** 8
                    for i, (l, r) in enumerate(Is):
                        if l <= p <= r and r < minr:
                            mini, minr = i, r
                    Is.pop(mini)
    print("Case #{}: {}".format(t + 1, ans))
