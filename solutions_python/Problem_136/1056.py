tcnum = int(input())

for tc in range(tcnum):
    cost, cpsd, goal = [float(n) for n in input().split()]

    cps = 2.0
    time = 0.0
    while True:
        if goal / cps <= cost / cps + goal / (cps + cpsd):
            time += goal / cps
            break
        time += cost / cps
        cps += cpsd

    print("Case #{}: {:.7f}".format(tc + 1, time))
