for tc in range(int(input())):
    N, P = map(int, input().split())
    G = map(int, input().split())
    d = [0] * P
    for i in G:
        d[i % P] += 1
    r = 0
    if P == 2:
        r += d[0]
        r += (d[1] + 1) // 2
    elif P == 3:
        r += d[0]
        p, q = min(d[1], d[2]), max(d[1], d[2])
        r += p
        r += (q - p + 2) // 3
    elif P == 4:
        r += d[0]
        p, q = min(d[1], d[3]), max(d[1], d[3])
        r += p
        s, w = d[2] // 2, q - p
        r += s
        if d[2] % 2 == 1:
            if 2 <= w:
                r += 1
                w -= 2
            elif w == 0:
                r += 1
        r += (w + 3) // 4
    print("Case #{}: {}".format(tc + 1, r))
