#! python3

from os import system

import sys
sys.stdout = open("output.txt", "w")

f = open("A-small-attempt0.in", "r")
input = f.read().strip()
# input = """4
# 4 11111
# 1 09
# 5 110011
# 0 1"""

input = input.split('\n')
del input[0]

for lineIndex, line in enumerate(input):
    lineInfo = line.split(' ')
    friendsNeeded = 0
    clappingTotal = 0
    for index, level in enumerate(lineInfo[1]):
        if level == "0" and index != 0:
            continue   
        # print(index, clappingTotal)
        if index > clappingTotal:
            friendsNeeded += index - clappingTotal
            clappingTotal += friendsNeeded
        clappingTotal += int(level)
    print("Case #" + str(lineIndex + 1) + ": " + str(friendsNeeded))

# system("pause")