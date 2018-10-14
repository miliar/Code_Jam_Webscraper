# GET FILE #
cases = open("B-large.in").readlines()[1:]
outputFile = open("B.out","w")
caseCount = 1
# GET FUNCTION #

def rule(num):
    index = 0
    prev = str(num)[0]
    for number in str(num)[1:]:
        if int(number) < int(prev):
            return index
        else:
            prev = number
            index += 1
    return "tidy"

def getStr(l):
    s = ""
    for i in l:
        s += str(i)
    return s

# TEST EACH CASE #
for case in cases:
    tidyNum = [num for num in str(int(case))]
    responce = rule(getStr(tidyNum))
    while responce != "tidy":
        tidyNum[responce] = int(tidyNum[responce]) - 1
        tidyNum[responce+1:] = ["9" for i in tidyNum[responce+1:]]
        responce = rule(getStr(tidyNum))
    outputFile.write("Case #" + str(caseCount) + ": " + str(int(getStr(tidyNum))) + "\n")
    caseCount += 1