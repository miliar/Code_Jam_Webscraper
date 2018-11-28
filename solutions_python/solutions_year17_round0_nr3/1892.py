import re
import sys
import operator

for i in range(0, int(input())):
    line = sys.stdin.readline().rstrip()
    line = line.split(' ')

    stallsString = '1' + '0'*int(line[0]) + '1'
    numPeople = int(line[1])

    for j in range(0, numPeople):
        optionsArray = stallsString.split('1')
        maxIndex, maxGroup = max(enumerate(optionsArray), key=operator.itemgetter(1))
        spotChoosing = len(maxGroup)//2
        maxGroup = maxGroup[:spotChoosing] + '1' + maxGroup[spotChoosing+1:]
        if (j+1 == numPeople):
            maxOnLeft = len(maxGroup[:spotChoosing])
            minOnRight = len(maxGroup[spotChoosing+1:])
            print("Case #{0}: {1} {2}".format(i+1, maxOnLeft, minOnRight))
            break
        optionsArray[maxIndex] = maxGroup
        stallsString = '1'.join(optionsArray)

