cases = int(raw_input())

for i in range(1, cases+1):
    (C, F, X) = tuple([float(j) for j in raw_input().split()])
    currSpeed = 2.0
    currTime = 0.0
    while True:
        timeWithoutFarm = X / currSpeed
        timeWithFarm = C / currSpeed + X / (currSpeed + F)
        if timeWithFarm < timeWithoutFarm:
            currTime += C / currSpeed
            currSpeed += F
        else:
            currTime += timeWithoutFarm
            break
    print "Case #%d: %.7f" % (i, currTime)