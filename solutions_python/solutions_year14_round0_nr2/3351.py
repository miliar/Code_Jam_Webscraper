from time import sleep

f = open("file.txt")
for i in range(int(f.readline())):
    params = f.readline().split(" ")
    farmCost = float(params[0])
    farmProductivity = float(params[1])
    neededCookies = float(params[2])
    currentProductivity = 2
    currentBest = 0
    newBest = neededCookies/currentProductivity
    farms = 1
    while True:
        currentBest = newBest
        time = 0
        for j in range(farms):
            time += farmCost/currentProductivity
            currentProductivity += farmProductivity
        newBest = time + neededCookies/currentProductivity
        if (newBest > currentBest): break
        farms += 1
        currentProductivity = 2
    caseOut = "Case #%i: %.7f" % (i+1, currentBest)
    a = open("out.txt", 'a')
    a.write(caseOut + "\n")
    a.close()
f.close()
