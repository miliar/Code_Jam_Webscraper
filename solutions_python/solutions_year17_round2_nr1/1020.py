t = int(input())

for case in range(t):

    lineData = input()
    lineData = lineData.split()

    horses = int(lineData[1])
    dist = int(lineData[0])


    longestTime = 0

    for _ in range(horses):

        hData = input()
        hData = hData.split()

        distRem = dist - int(hData[0])
        spd = int(hData[1])

        thisTime = distRem / spd

        if thisTime > longestTime:
            longestTime = thisTime


    out = dist/longestTime
    print("Case #" + str(case+1) + ": " + "{0:.6f}".format(out))
