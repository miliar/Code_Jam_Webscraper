t = int(input())
for testcase in range(t):
    D, N = map(int,input().split(' '))
    horse = []
    maxTime = 0
    for numHorse in range(N):
        horse.append(input().split(' '))

    for h in range(N):
        dis = int(horse[h][0])
        sp = float(horse[h][1])
        time = (D - dis)/sp
        if maxTime < time:
            maxTime = time
    ans = D/maxTime
    print("Case #%s: %0.6f" %(str(testcase + 1),ans))