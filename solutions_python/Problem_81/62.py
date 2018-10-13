T = int(input())

for t in range(T):
    N = int(input())
    schedule = []
    for n in range(N):
        schedule.append(list(input()))
    wins = []
    losses = []
    WP = []
    for n in range(N):
        wins.append(schedule[n].count("1"))
        losses.append(schedule[n].count("0"))
        WP.append(wins[-1] / (wins[-1] + losses[-1]))
    OWP = []
    for n in range(N):
        allOWP = []
        for m in range(N):  # opponent
            if schedule[m][n] == "1":
                allOWP.append((wins[m] - 1) / (wins[m] + losses[m] - 1))
            elif schedule[m][n] == "0":
                allOWP.append((wins[m]) / (wins[m] + losses[m] - 1))
        OWP.append(sum(allOWP) / len(allOWP))
    OOWP = []
    for n in range(N):
        allOOWP = []
        for m in range(N):
            if schedule[n][m] != ".":
                allOOWP.append(OWP[m])
        OOWP.append(sum(allOOWP) / len(allOOWP))
    print("Case #{}:".format(t + 1))
    for n in range(N):
        print(0.25 * WP[n] + 0.50 * OWP[n] + 0.25 * OOWP[n])