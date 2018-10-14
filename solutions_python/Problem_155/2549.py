import sys
import fileinput
numTries = int(raw_input())
sys.setrecursionlimit(2000)

def find_num(arrNum, reserve, required):
    if reserve >= len(arrNum):
        return required
    if reserve > 0:
        newReserve = sum(arrNum[0:reserve])
        return find_num(arrNum[reserve:], newReserve, required)
    if reserve == 0:
        if int(arrNum[0]) == 0:
            return find_num(arrNum[1:], reserve, required+1)
        else:
            return find_num(arrNum[1:], reserve + int(arrNum[0]) -1, required)
    return 1337

for line in range(numTries):
    (maxLvl, stringNum) = raw_input().split(" ")
    arrNum = map(int, list(stringNum))
    print "Case #"+str(line+1)+": "+str(find_num(arrNum, 0, 0))
