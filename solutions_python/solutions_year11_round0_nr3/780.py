import sys
numTest = int(sys.stdin.readline())
for _ in range(numTest):
    out = "Case #%d: " % (_ + 1)
    numOfNum = int(sys.stdin.readline())
    inputList = [ int(c) for c in sys.stdin.readline().strip().split() ]
    assert len(inputList) == numOfNum

    res = 0
    for __ in inputList:
        res = res ^ __
    if res != 0:
        out += "NO"
        print out
    else:
        bother = min(inputList)
        out +=  str(sum(inputList) - bother)
        print out

