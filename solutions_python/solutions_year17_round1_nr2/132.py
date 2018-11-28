T = int(raw_input());
for t in range(1, T+1):
    N, P = map(int, raw_input().split())

    r = map(int, raw_input().split())
    q = [list(map(int, raw_input().split())) for _ in range(N)]

    cnt = 0

    qs = []
    for line, R in zip(q, r):
        tmp = []
        for value in line:
            u =(value * 10) // 9 // R
            l = (value * 10 + 11*R - 1 )// 11 // R
            # 9*R*number <= 10*value
            # number <= 10*value / R / 9
            if l <= u:
                tmp.append((l, u))
        qs.append(tmp)

    events = []
    for i in range(N):
        for j in range(len(qs[i])):
            events.append((qs[i][j][0], 0, i, j))
            events.append((qs[i][j][1], 1, i, j))

    events.sort()
    
    x = [0 for _ in range(N)]
    y = [0 for _ in range(N)]

    for event in events:
        pos, startstop, i, j = event
        if startstop == 0:
            x[i] += 1
            if all(x):
                cnt += 1
                x = [z-1 for z in x]
                y = [z+1 for z in y]
        else:
            if y[i]:
                y[i] -= 1
            else:
                x[i] -= 1

    print("Case #{}: {}".format(t, cnt))

# }
