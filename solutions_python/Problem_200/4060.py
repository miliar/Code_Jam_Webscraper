import numpy
lines = open('small.input', 'r').read().splitlines()
numberOfCases = int(lines[0])

with open('output.txt', 'w') as out:
    for number in range(numberOfCases):
        findTidy = lines[number+1]
        while True:
            tidyList = numpy.array(list(findTidy))
            lenth = len(tidyList)
            allNotSet = False
            for i in range(1, lenth):
                if not tidyList[i-1] <= tidyList[i]:
                    tidyList[i-1] = int(tidyList[i-1]) - 1
                    tidyList[i:] = 9
                    allNotSet = True
                    findTidy = list(tidyList)
                    break
            if not allNotSet:
                break

        print 'Case #{}: {}'.format(number+1, int(''.join(tidyList)))
