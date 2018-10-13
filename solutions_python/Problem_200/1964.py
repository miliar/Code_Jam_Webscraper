import re
import sys

for i in range(0, int(input())):
    line = sys.stdin.readline().rstrip()

    tidyNotFound = True

    while tidyNotFound:
        if (line[0] == '0'):
            line = line[1:]
        if (len(line) == 1):
            print("Case #{0}: {1}".format(i+1, line))
            tidyNotFound = False
        for j in range(0, len(line) - 1):
            if (int(line[j]) > int(line[j+1])):
                startIndex = re.search(r"[{0}]+".format(line[j]), line).start()
                line = line[:startIndex] + str(int(line[startIndex]) - 1) + "9"*len(line[startIndex+1:])
                break
            elif (j == len(line) - 2):
                print("Case #{0}: {1}".format(i+1, line))
                tidyNotFound = False
                break
