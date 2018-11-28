# 0th solution to Problem B

t = int(input())

def m(x):
    while x <= 0:
        x += 1440
    while x > 1440:
        x-= 1440
    return x

def solve():
    C, J = map(int, input().split(' '))
    t = []
    for a in range(C):
        s, e = map(int, input().split(' '))
        t.append((s, e, True))
    for a in range(J):
        s, e = map(int, input().split(' '))
        t.append((s, e, False))
    t = sorted(t)

    res = 0

    looseIntervals = 0
    nonLooseIntervalsC = []
    nonLooseIntervalsJ = []
    forcedIntervalsC = 0
    forcedIntervalsJ = 0

    it = 1
    while it < len(t):
        if not t[it][2]:
            forcedIntervalsC += t[it][1]-t[it][0]
        if t[it][2]:
            forcedIntervalsJ += t[it][1]-t[it][0]

        if t[it][2] and t[it-1][2]:
            nonLooseIntervalsJ.append(t[it][0]-t[it-1][1])
        elif not t[it][2] and not t[it-1][2]:
            nonLooseIntervalsC.append(t[it][0]-t[it-1][1])
        else:
            looseIntervals += t[it][0]-t[it-1][1]
            res += 1
        it += 1

    # it = 0:
    if not t[0][2]:
        forcedIntervalsC += t[0][1] - t[0][0]
    if t[0][2]:
        forcedIntervalsJ += t[0][1] - t[0][0]
    if t[0][2] and t[-1][2]:
        nonLooseIntervalsJ.append(1440 - t[-1][1] + t[0][0])
    elif not t[0][2] and not t[- 1][2]:
        nonLooseIntervalsC.append(1440 - t[-1][1] + t[0][0])
    else:
        looseIntervals += 1440 - t[-1][1] + t[0][0]
        res += 1

    #print(forcedIntervalsC, looseIntervals, res, nonLooseIntervalsC, nonLooseIntervalsJ)

    res2 = res

    ct = 1440 - looseIntervals - forcedIntervalsJ
    nonLooseIntervals = nonLooseIntervalsC + nonLooseIntervalsJ
    nonLooseIntervals = sorted(nonLooseIntervals, key=lambda x: -x)
    it = 0
    while ct > 720:
        ct -= nonLooseIntervals[it]
        res += 2
        it += 1

    jt = 1440 - looseIntervals - forcedIntervalsC
    nonLooseIntervals = nonLooseIntervalsC + nonLooseIntervalsJ
    nonLooseIntervals = sorted(nonLooseIntervals, key=lambda x: -x)
    it = 0
    while jt> 720:
        jt -= nonLooseIntervals[it]
        res2 += 2
        it += 1
    return max(res, res2)


    # nevermind that:

    if forcedIntervalsC <= 720 and forcedIntervalsC >= 720 - looseIntervals:
        return res

    if forcedIntervalsJ <= 720 and forcedIntervalsJ >= 720 - looseIntervals:
        return res



    else:
        res2 = res
        forcedIntervalsC += looseIntervals
        nonLooseIntervalsC = sorted(nonLooseIntervalsC, key=lambda x: -x)
        it = 0
        while forcedIntervalsC < 720:
            print(forcedIntervalsC)
            forcedIntervalsC += nonLooseIntervalsC[it]
            it += 1
            res += 2
            if forcedIntervalsC < 720:
                return res
            if it >= len(nonLooseIntervalsC):
                break

        res = res2
        forcedIntervalsJ += looseIntervals
        nonLooseIntervalsJ = sorted(nonLooseIntervalsJ, key=lambda x: -x)
        it = 0
        while forcedIntervalsJ < 720:
            print(forcedIntervalsJ)
            forcedIntervalsJ += nonLooseIntervalsJ[it]
            it += 1
            res += 2
            if forcedIntervalsJ < 720:
                return res
            if it >= len(nonLooseIntervalsJ):
                break




for a0 in range(t):
    sol = solve()
    print("Case #" + str(a0 + 1) + ": " + str(sol))
