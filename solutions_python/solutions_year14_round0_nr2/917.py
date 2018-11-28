prefix = "B-large"
postfixIn = ".in"
postfixOut = ".out"

fileIn = open(prefix + postfixIn, "r")
lines = fileIn.readlines()
fileIn.close()

results = []
template = "Case #%d: %s\n"

############################################################

casesCount = int(lines[0].strip())
for i in xrange(casesCount):
    [cost, extra, goal] = [float(elem) for elem in lines[i + 1].strip().split()]
    productivity = 2.0
    producedCookies = 0.0
    # print cost, extra, goal
    totalTime = 0.0
    goalProductivity = extra * (goal - cost) / cost
    while productivity <= goalProductivity:
        totalTime += cost / productivity
        productivity += extra
    totalTime += goal / productivity

    # print totalTime
    result = template % (i + 1, str(totalTime))
    results.append(result)

############################################################

fileOut = open(prefix + postfixOut, "w")
for result in results:
    fileOut.write(result)
fileOut.close()
