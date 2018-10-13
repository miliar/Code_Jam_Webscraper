#!/opt/local/bin/python3.1

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    p = []
    for i in range(N):
        p.append([int(x) for x in input().split()])
    c = set()
    for i in range(N):
        for j in range(i):
            di = p[i][1] - p[i][0]
            dj = p[j][1] - p[j][0]
            dx = p[j][0] - p[i][0]
            if di - dj != 0:
                dt = dx / (di - dj)
                if 0.0 <= dt <= 1.0:
                    c.add((dt, p[i][0] + di * dt))
    print("Case #{}: {}".format(t, len(c)))
