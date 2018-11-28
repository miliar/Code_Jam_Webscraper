TIDY = -1


def addingCase(n, text):
    resultCase = "Case #" + str(n) + ": " + str(text) + "\n"
    print resultCase
    return resultCase


def nextPosibleNumber(result, wrongI):
    resultString = str(result)
    length = len(resultString)

    minus = int(resultString[wrongI:length]) + 1
    print "minus", str(minus)
    return result - minus


def tidy(n):
    nString = str(n)
    for i in range(0, len(nString) - 1):
        if (int(nString[i]) > int(nString[i+1])):
            print "no tidy", n
            return i
    return TIDY


def lastTidyNumber(n):

    result = n
    print result
    tries = 0
    while (result >= 10):
        wrongI = tidy(result)
        if (wrongI == TIDY):
            return result
        else:
            result = nextPosibleNumber(result, wrongI + 1)
        tries = tries + 1
    return result


inFile = open("B-large.in", "r")
outFile = open("B-large.out", "w")

t = int(inFile.readline())
print "number of test cases is", t

icase = 1
while icase <= t:
    n = int(inFile.readline())
    outFile.write(addingCase(icase, lastTidyNumber(n)))
    icase = icase + 1


outFile.close()
inFile.close()
