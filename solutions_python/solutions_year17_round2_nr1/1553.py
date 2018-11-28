t = int(input())
for test in range(1, t+1):
    D, n = (int(x) for x in input().split())
    horses = []
    time = []

    for x in range(n):
        k, s = (int(x) for x in input().split())
        timeTaken = (D - k)/float(s)
        time.append(timeTaken)
        horses.append([k, s])

    maxTime = max(time)

    speed = D/float(maxTime)

    print(str("Case #") + str(test)+ ":", str(speed))