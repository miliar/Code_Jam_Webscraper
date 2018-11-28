import os
import heapq
import math




def getResultMultiLine():
    pass

# [0, 1, 2]: (-3, 0) -> [0] (-1, 0), [2] (-1, 2)
# [0, 1, 2, 3]: (-4, 0) -> [0] (-1, 0), [2, 3] (-2, 2)
def simulate(n):
    parts = [(-n, 0)]
    heapq.heapify(parts)
    for i in range(n):
        (size, pos) = heapq.heappop(parts)
        size = -size
        len1 = getLength(n, i + 1)
        if len1 != size:
            print "Mismatch", len1, size
        pos1 = pos + (size - 1) / 2
        size1 = pos1 - pos
        size2 = pos + size - pos1 - 1
        heapq.heappush(parts, (-size1, pos))
        heapq.heappush(parts, (-size2, pos1 + 1))
#         print pos1, "left", pos1 - pos, "right", pos + size - pos1 - 1, parts
        
    
def getLength(n, k):
    p = int(math.floor(math.log(k) / math.log(2) + 1e-12))
    p2 = 1 << p
    len1 = (n - p2 + 1) / p2
    if k - p2 < (n - p2 + 1) % p2:
        return len1 + 1
    else:
        return len1

def getResult(n, k):
    # simulate(n)
    len1 = getLength(n, k)
    return str(len1 / 2) + " " + str((len1 - 1) / 2)
        
    

input = """
5
4 2
5 2
6 2
1000 1000
1000 1
"""



if __name__ == "__main__":
    problem = os.path.basename(__file__)[0]
    folder = os.path.dirname(__file__)
    nameParts = [os.path.join(folder, problem + "-" + name) for name in ["test", "small-1-attempt0", "small-2-attempt0", "large"]]
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
        
        testCase = map(int, lines[iLine].split())
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
