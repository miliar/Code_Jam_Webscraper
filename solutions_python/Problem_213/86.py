def solve(test_num):
    n, c, m = map(int, input().split())
    rides = 0
    promotions = 0
    tickets = [[0] * (n + 1), [0] * (n + 1)]
    for i in range(m):
        p, b = map(int, input().split())
        tickets[b - 1][p] += 1
    while tickets[0][1] > 0:
        rides += 1
        tickets[0][1] -= 1
        best = 0
        s = 0
        for i in range(2, n + 1):
            if tickets[1][i] > 0 and tickets[0][i] + tickets[1][i] > s:
                s = tickets[0][i] + tickets[1][i]
                best = i
        if best > 0:
            tickets[1][best] -= 1
    while tickets[1][1] > 0:
        rides += 1
        tickets[1][1] -= 1
        best = 0
        s = 0
        for i in range(2, n + 1):
            if tickets[0][i] > 0 and tickets[0][i] + tickets[1][i] > s:
                s = tickets[0][i] + tickets[1][i]
                best = i
        if best > 0:
            tickets[0][best] -= 1
    add_rides = max(sum(tickets[0]), sum(tickets[1]))
    s = 0
    for i in range(2, n + 1):
        if tickets[0][i] + tickets[1][i] > s:
            s = tickets[0][i] + tickets[1][i]
    if s > add_rides:
        promotions = s - add_rides

    print("Case #", test_num, ": ", rides + add_rides, " " , promotions, sep='')

for i in range(1, int(input()) + 1):
    solve(i)

