import sys

def solveCase(t):
    Ac, Aj = map(int, sys.stdin.readline().split())
    times = []

    Cc = 0
    
    for i in range(Ac):
        c, d = map(int, sys.stdin.readline().split())
        Cc += d - c  

        times.append((c, d, 0))

    for i in range(Aj):
        c, d = map(int, sys.stdin.readline().split())
        Cc -= d - c

        times.append((c, d, 1))

    times.sort()

    curSwaps = 0
    curAct = times[-1][2]
    
    extraSwapTimes = [[], []]
    
    curUnassigned = 0
    prevEndTime = times[-1][1] - 1440

    for i in range(Ac + Aj):
        if times[i][2] != curAct:
            curSwaps += 1
            curAct = times[i][2]
            curUnassigned += times[i][0] - prevEndTime
        else:
            extraSwapTimes[times[i][2]].append(times[i][0] - prevEndTime)
            if curAct == 0:
                Cc += times[i][0] - prevEndTime
            else:
                Cc -= times[i][0] - prevEndTime

        prevEndTime = times[i][1]


    if Cc > 0:
        Cc -= min(curUnassigned, Cc)
        extraSwapTimes = extraSwapTimes[0]
    else:
        Cc += min(curUnassigned, abs(Cc))
        extraSwapTimes = extraSwapTimes[1]
        
    extraSwapTimes.sort(reverse=True)
    Cc = abs(Cc)
    i = 0
    while Cc > 0:
        Cc -= extraSwapTimes[i] * 2
        i += 1
        curSwaps += 2


    print("Case #" + str(t) + ": " + str(curSwaps))

T = int(sys.stdin.readline())


for i in range(T):
    solveCase(i + 1)
