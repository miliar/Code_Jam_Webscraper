# import sys
# import time
# sys.setrecursionlimit(100000)

# filename = "R1B-01-input-test"
filename = "R1B-01-small-attempt1"
# filename = "R1-01-A-large-practice"
fi = open(filename+'.in', 'r')
cases = list()
debug = True
# collect = ""
index = 0
# strVal = 0

subset = list()
subindex = 0
nextgoal = 0
for line in fi:
    # print index % 3
    if (index > 0):
        if (index == 1) or (subindex == nextgoal):
            nextgoal = int(line)
            subindex = 0
            if (index > 2):
                cases.append(subset)
                subset = list()
        else:
            subset.append(line.strip())
            subindex = subindex + 1

    index = index + 1
cases.append(subset)

fi.close()
# print cases



def removeDuplicates(lines):
    noDupList = list()
    noDupSet = set()
    noDupSetFinal = set()
    for line in lines:
        noDupList.append(list(set(list(line))))
    for line in noDupList:
        noDupSet.add(''.join(line))
    # print noDupSet
    # return True
    if len(noDupSet) == 1:
        for line2 in lines:
            newLine = str(line2)
            for char in list(list(noDupSet)[0]):
                for i in range(len(newLine)-1):
                    newLine = newLine.replace(char*2, char)
                # print char*2, line2, newLine, "\n"
            print "L", line2, "LN", newLine
            noDupSetFinal.add(newLine)
        print "noDupSetFinal", noDupSetFinal
        return len(noDupSetFinal) == 1
    else:
        return False

def processStrings(lines):

    countLetters = list()
    # caseLetters = list()

    for line in lines:
        prevChar = ""
        index = 0
        caseLetters = list()
        for char in list(line):
            if prevChar != char:
                # print char
                if index > 0:
                    caseLetters.append(index)
                index = 1
                prevChar = char
            else:
                index += 1
        caseLetters.append(index)
        countLetters.append(caseLetters)

    # print lines, "Len", map(len, countLetters), len(set(lines[0])), len(set(lines[1]))
    return countLetters

def checkEq(digits):
    fList = digits[0]
    for dList in digits:
        if (dList != fList):
            return False
    return True

def getRes(digits):
    # print digits, len(digits[0]), len(digits[1]), len(digits[2])
    fList = digits[0]
    # grandRes = 0
    result = 0

    for i in range(len(fList)):
        # result = 0
        allNums = list()
        for dList in digits:
            allNums.append(dList[i])
                # return False

        avg = reduce(lambda x, y: x + y, allNums) / (1.0*len(allNums))
        closest = min(allNums, key=lambda x:abs(x-avg))
        # print "Avg", allNums, "=", avg, "; Clo=", closest
        for num in allNums:
            result += abs(closest - num)
        # grandRes += result
    return result

index = 1
solution = ""

for case in cases:
    if removeDuplicates(case):
        digitRepresent = processStrings(case)
        solRes = 0
        if not checkEq(digitRepresent):
            solRes = getRes(digitRepresent)

        solution = solution + "Case #" + str(index) + ": " + str(solRes) + '\n'
    else:
        solution = solution + "Case #" + str(index) + ': Fegla Won\n'
# 	sol_object = processCookies(case)
# 	# print index, ":::", sol_object
# 	# if index == 1:
# 		# print index, ":::", sol_object
    # print "Case", index, time.clock()#, "\n",case, "\n"
    # if isDatasetOperatable(case):
    #     solNum = processCharge(case)
    #     solStr = str(solNum) if (solNum >= 0) else "NOT POSSIBLE"
    #     solution = solution + "Case #" + str(index) + ": " + solStr + '\n'
    # else:
    #     solution = solution + "Case #" + str(index) + ": NOT POSSIBLE" + '\n'
    # print "SOL:",solStr, "\n"

    # if index == 31:
    #     print "Case", index, "\n",case, "\n"
    #     break
    index = index + 1

print solution
fo = open(filename+'.out', 'w')
solution = solution.strip()
fo.write(solution)
fo.close()
