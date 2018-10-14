lastIChange = -1


def addingCase(n, text):
    resultCase = "Case #" + str(n) + ": " + text + "\n"
    print resultCase
    return resultCase


def minimumK(K):
    if (K % 2 == 0):
        return K / 2
    return (K / 2) + 1


def flipK(pancakes, i, K):
    lenght = len(pancakes)
    flipping = pancakes[i:i+K]
    # print "flipping", flipping
    flipping = ''.join('+' if x == '-' else '-' for x in flipping)
    # print pancakes[0:i], flipping, pancakes[i+K:lenght]
    return pancakes[0:i] + flipping + pancakes[i+K:lenght]


def exec_maneuver(pancakes, K):
    lenght = len(pancakes)
    for i in range(0, lenght):
        if (pancakes[i] == "-"):
            print "lastIChange", lastIChange, " i + K: ", i + K
            if (i + K > lenght or lastIChange >= i):
                return "IMPOSSIBLE"
            lastIChange = i
            return flipK(pancakes, i, K)
    return "IMPOSSIBLE"


def numbersExecutionManeuver(pancakes, K):
    result = 0
    happyFacePancakes = "+" * len(pancakes)
    # print "happyFacePancakes", happyFacePancakes
    lastIChange = -1
    while (pancakes != happyFacePancakes and pancakes != "IMPOSSIBLE"):
        result += 1
        lenght = len(pancakes)
        for i in range(0, lenght):
            if (pancakes[i] == "-"):
                if (i + K > lenght or lastIChange > i):
                    return "IMPOSSIBLE"
                lastIChange = i
                pancakes = flipK(pancakes, i, K)
                break
        print "after maneuver: " + pancakes

    if (pancakes == "IMPOSSIBLE"):
        return "IMPOSSIBLE"
    return str(result)


inFile = open("A-large.in", "r")
outFile = open("A-large.out", "w")

t = int(inFile.readline())
print "number of test cases is", t

print "testing ", 15 / 2
icase = 1
while icase <= t:
    line = inFile.readline().split(" ")
    pancakes = line[0]
    K = int(line[1])
    print "n is '" + pancakes + "' and K is " + str(K)
    outFile.write(addingCase(icase, numbersExecutionManeuver(pancakes, K)))
    icase = icase + 1


outFile.close()
inFile.close()
