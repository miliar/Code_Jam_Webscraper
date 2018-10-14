tc = int(input())
for etc in range(tc):
    D, N = map(int, input().strip().split())
    horse = []
    for i in range(N):
        loc, speed = map(int, input().strip().split())
        horse.append((loc, speed))
    horse = sorted(horse, key = lambda x: -x[0])
    maxTime = 0
    for i in horse:
        time = (D - i[0])/i[1]
        if (time > maxTime):
            maxTime = time
    print ("Case #" + str(etc+1) + ": " + str(D/maxTime))
