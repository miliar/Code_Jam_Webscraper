def solve():
    Ac, Aj = map(int, raw_input().split())
    C = []
    D = []
    B = []
    for _ in range(Ac):
        s, e = map(int, raw_input().split())
        C.append((s,e))
        B.append((s,e, 0))
    for _ in range(Aj):
        s, e = map(int, raw_input().split())
        D.append((s,e))
        B.append((s,e, 1))

    C.sort()
    D.sort()
    B.sort()

    if Ac == 2:
        (s1, e1), (s2, e2) = C
        if (e2 - s1) <= 720 or e1+1440-s2 <= 720:
            return 2
        else:
            return 4

    if Aj == 2:
        (s1, e1), (s2, e2) = D
        if (e2 - s1) <= 720 or e1+1440-s2 <= 720:
            return 2
        else:
            return 4

    return 2





T = int(raw_input())
for t in range(1, T+1):
    print "Case #{}: {}".format(t, solve())
