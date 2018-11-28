__author__ = 'Mike'

import pprint


pp = pprint.PrettyPrinter(indent=2)

class caseA :

    def __init__(self):
        self.caseNum = 0
        self.maxShyness = 0;

        # array of shyness=>count
        self.audience = {}

def getCases(filename):
    cases = []
    f = open(filename, 'r')
    caseCount = 0
    lineNum = 0
    for line in f :
        line = line.rstrip('\n')
        #pp.pprint(line)
        #pp.pprint(lineNum)
        if lineNum == 0 :
            caseCount = int(line)
            lineNum += 1
            continue
        case = caseA()
        tokens = line.split()
        case.caseNum = lineNum
        case.maxShyness = int(tokens[0])

        # read each digit of the data
        for i in range(0, case.maxShyness + 1) :
            case.audience[i] = int(tokens[1][i])

        cases.append(case)
        lineNum += 1

    if(len(cases) != caseCount) :
        print("Wrong cases count!")


    return cases

def getMinAudienceAdded(case):
    additionalAudience = 0
    totalClapping = 0
    #go through the shyness levels
    for level in range(0, case.maxShyness + 1) :
        if totalClapping >= level :
            totalClapping += case.audience[level]
        else :
            neededtoAdd = level - totalClapping
            additionalAudience += neededtoAdd
            totalClapping += neededtoAdd
            totalClapping += case.audience[level]

    return additionalAudience

    pass

def main():
    file = "A-large"
    cases = getCases(file + ".in")

    solution = ""

    outFile = open(file + '.output.txt', "w")

    for case in cases :
        ansLine = "Case #" + str(case.caseNum) + ": " + str(getMinAudienceAdded(case)) + "\n"
        pp.pprint(ansLine)
        outFile.write(ansLine)


    pass

if __name__ == "__main__":
    main()