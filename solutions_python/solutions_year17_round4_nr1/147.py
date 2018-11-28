import os
import heapq
import math
import re

def getResultMultiLine(h, w, qLines):
    pass

def getResult(n, p, groups):
    g = [v % p for v in groups]
    print g
    if p == 2:
        return n - sum(g) / 2
    elif p == 3:
        count1 = len([v for v in g if v % 3 == 1])
        count2 = len([v for v in g if v % 3 == 2])
        c1 = min(count1, count2)
        c2 = max(count1, count2)
        print c1, c2
        return n - c1 - (2 * ((c2 - c1) / 3) + (1 if (c2 - c1) % 3 == 2 else 0))
    elif p == 4:
        count1 = len([v for v in g if v % 4 == 1])
        count2 = len([v for v in g if v % 4 == 2])
        count3 = len([v for v in g if v % 4 == 3])
        bad = count2 / 2 + min(count1, count3)
        c2 = count2 % 2
        c1 = max(count1, count3) - min(count1, count3)
        print bad, c1, c2
        if c2 == 0:
            bad += c1 - (c1 + 3) / 4
        elif c1 >= 2:
            bad += 2 + (c1 - 2) - (c1 - 2 + 3) / 4
        else:
            bad += c1
        return n - bad
                

input = """
3
1 4
1
2 4
1 2
6 4
2 3 2 3 1 2
"""



if __name__ == "__main__":
    problem = os.path.basename(__file__)[0]
    folder = os.path.dirname(__file__)
    nameParts = [os.path.join(folder, problem + "-" + name) for name in ["test", "xsmall-attempt0", "large"]]
    namePart = None
    for namePart1 in nameParts:
        if os.path.exists(namePart1 + ".in"):
            namePart = namePart1
            print "Using " + namePart
    if namePart is None:
        lines = [s for s in input.split("\n") if len(s) > 0]
    else:
        lines = [s[:len(s) - 1] for s in open(namePart + ".in", "r")]
    count = int(lines[0])
    resultLines = []
    iLine = 1
    
    multiLineResult = False
    
    for iTry in range(count):
        iLastResult = len(resultLines)

        # input = ...
        # iLine += 1

        # input = map(int, lines[iLine].split())
        
        print lines[iLine]
        testCase = map(int, lines[iLine].split())
        (n, p) = testCase
        iLine += 1
        groups = map(int, lines[iLine].split())
        iLine += 1
        testCase.append(groups)

        if multiLineResult:
            resultLines.append("Case #" + str(iTry + 1) + ":")
            resultLines += map(str, getResultMultiLine(*testCase))
        else:
            resultLines.append("Case #" + str(iTry + 1) + ": " + str(getResult(*testCase)))
        for j in range(iLastResult, len(resultLines)):
            print resultLines[j]
    if namePart is not None:
        with open(namePart + ".out", "wt") as oFile:
            for resultLine in resultLines:
                oFile.write(resultLine + "\n")
