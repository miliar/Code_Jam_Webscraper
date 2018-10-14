import os





def getResultMultiLine():
    pass

def getResult(x):
    digits = map(int, [c for c in str(x)])
    n = len(digits)
    outDigits = []
    for n1 in range(n):
        x1 = int("".join(map(str, digits[n1:])))
        allOnes = int("".join(["1"] * (n - n1)))
        iMax = 9
        while iMax > 0 and iMax * allOnes > x1:
            iMax -= 1
        if iMax == 0:
            return int("".join(["9"] * (n - n1 - 1)))
        outDigits.append(iMax)
        if digits[n1] > iMax:
            outDigits += [9] * (n - n1 - 1)
            break
    return int("".join(map(str, outDigits)))
            
        
        
    

input = """
15
132
1000
7
111111111111111110
2341
1
2
3
10
11
12
90
91
98
99
"""



if __name__ == "__main__":
    problem = os.path.basename(__file__)[0]
    folder = os.path.dirname(__file__)
    nameParts = [os.path.join(folder, problem + "-" + name) for name in ["test", "small-attempt0", "large"]]
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
        
        testCase = [int(lines[iLine])]
        iLine += 1

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
