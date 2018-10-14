from math import floor, ceil

def run(n, cnt):
    num = 1
    prevDifCnt = 0
    prevStartedWithDif = False

    n -= 1
    i = 0
    while True:
        curr = [ceil(n/2), floor(n/2)]
##        if(curr[0] == curr[1]):
##            same = False
##        else:
##            same = True

        if(prevStartedWithDif):
            firstCnt = prevDifCnt
            secondCnt = num-prevDifCnt
        else:
            firstCnt = num-prevDifCnt
            secondCnt = prevDifCnt

        ##print("n =", n, ", firstCnt =", firstCnt, ", secondCnt =", secondCnt)

        if(curr[0] == curr[1]):
            prevStartedWithDif = False
            prevDifCnt = secondCnt
        else:
            prevStartedWithDif = True
            prevDifCnt = firstCnt
            
        for j in range(firstCnt):            
##            print(" ".join(str(val) for val in curr))
            i += 1
            if(i == cnt):
                return curr

        if(curr[0] > curr[1]):
            curr[0] -= 1
        else:
            curr[1] -= 1

        for j in range(secondCnt):
##            print(" ".join(str(val) for val in curr))
            i += 1
            if(i == cnt):
                return curr

        n = curr[1]
        num *= 2

inFile = open("C-small-2-attempt0.in")
outFile = open("C-small-2-attempt0.out", "w")

cnt = int(inFile.readline().rstrip())

for i in range(1, cnt+1):
    (n, cnt) = (int(val) for val in inFile.readline().rstrip().split())
    result = run(n, cnt)
    print("Case #" + str(i) + ": " + " ".join(str(val) for val in result), file=outFile)

outFile.close()
