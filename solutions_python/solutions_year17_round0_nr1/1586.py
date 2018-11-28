import os





def getResultMultiLine():
    pass

def getResult(line, k):
    if len(line) < k:
        return "IMPOSSIBLE"
    bits = [c == "+" for c in line]
    count = 0
    for i in range(len(line) - k + 1):
        if not bits[i]:
            for j in range(i, i + k):
                bits[j] = not bits[j]
            count += 1
    for i in range(len(line) - k + 1, len(line)):
        if not bits[i]:
            return "IMPOSSIBLE"
    return count

input = """
5
---+-++- 3
+++++ 4
-+-+- 4
--+-- 3
-+-+- 3
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
        
        testCase = lines[iLine].split()
        testCase[1] = int(testCase[1])
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
