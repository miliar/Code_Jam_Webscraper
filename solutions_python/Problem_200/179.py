from __future__ import print_function

def solveProblem(k):
    last = k

    #Check if k is ok
    #convert k to a string
    strK = str(k)
    #convert the string to a list
    #probabily could have just used % instead
    listK = [int(x) for x in strK]

    #assume violated
    violated = True
    while violated:

        #Start from the left to right and find the fist violation
        for i in xrange(len(listK) - 1):
            if listK[i] > listK[i+1]:
                listK[i] -= 1
                #set everything behind the 1 to 9
                for j in xrange(len(listK) - 1 - i):
                    listK[i + j + 1] = 9

        #Check for violation
        violated = False
        for i in xrange(len(listK) - 1):
            if listK[i] > listK[i+1]:
                violated = True
    print(listK)

    #Reassemble the integer
    resultStrK = ""
    for i in listK:
        resultStrK += str(i)
    resultStrK = resultStrK.lstrip('0')
    print(resultStrK)
    return [resultStrK]

import sys

def main():
    inPath = sys.argv[1]
    outPath = inPath.split('.')[0] + '.out'
    file = open(inPath, "r")
    out = open(outPath, "w")
    case = 0
    #Read Input File
    for line in file:
        #Skip first line
        if case == 0:
            case += 1
            continue

        #solve problem
        input = int(line)
        result = solveProblem(input)
        #format Problem
        resultStr = ""
        for r in result:
            resultStr += str(r) + ' '
        print('Case #{case}: {resultStr}'.format(case=case, resultStr=resultStr), file=out)
        case += 1

if __name__ == "__main__":
    main()