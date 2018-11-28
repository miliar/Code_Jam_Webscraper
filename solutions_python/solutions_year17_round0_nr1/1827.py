import re
import sys

for i in range(0, int(input())):
    line = sys.stdin.readline().rstrip()
    line = line.split(" ")

    isImpossible = False
    flipLimit = int(line[1])
    startIndex = 0
    numFlips = 0

    while True:
        if (re.match(r"[+]*$", line[0])):
            break

        newStartIndex = re.search(r"-[+-]{{0}}".format(flipLimit-1), line[0]).start()
        if (newStartIndex < startIndex):
            isImpossible = True
            break
        startIndex = newStartIndex

        if (startIndex <= len(line[0])-flipLimit):
            for j in range(startIndex, startIndex + flipLimit):
                if line[0][j] == '+':
                    line[0] = line[0][:j] + '-' + line[0][j+1:]
                elif line[0][j] == '-':
                    line[0] = line[0][:j] + '+' + line[0][j+1:]
            numFlips += 1
        else:
            isImpossible = True
            break

        if ("-" in line[0][:flipLimit] and startIndex == len(line[0])-flipLimit):
            isImpossible = True
            break

    if (isImpossible):
        print("Case #{0}: ".format(i+1) + "IMPOSSIBLE")
    else:
        print("Case #{0}: ".format(i+1) + str(numFlips))