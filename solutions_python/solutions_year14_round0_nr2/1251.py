trials = int(raw_input())

for i in range(1, trials+1):
    
    line = raw_input().split()
    C = float(line[0])
    F = float(line[1])
    X = float(line[2])
    
    timestore = 0.0
    upgrades = 0
    
    while True:

        nextUpgradeTime = C/(2+F*upgrades)
        nextUpgradeScore = nextUpgradeTime + X/(2+F*(upgrades+1))
        finishItTime = X/(2+F*upgrades)

        if nextUpgradeScore < finishItTime:
            timestore += nextUpgradeTime
            upgrades += 1
        else:
            timestore += finishItTime
            break

    print "Case #" + str(i) + ": " + str(timestore)