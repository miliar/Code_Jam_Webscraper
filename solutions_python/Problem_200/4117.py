import numpy
lines = open('input.txt', 'r').read().splitlines()
numberOfCases = int(lines[0])

with open('output.txt', 'w') as out:
    for number in range(numberOfCases):
        findNumber = lines[number+1]
        while True:
            finalList = numpy.array(list(findNumber))
            length = len(finalList)
            found = False
            for i in range(1, length):
                if not finalList[i-1] <= finalList[i]:
                    finalList[i-1] = int(finalList[i-1]) - 1
                    finalList[i:] = 9
                    found = True
                    findNumber = list(finalList)
                    break
            if not found:
                break

        print 'Case #{}: {}'.format(number+1, int(''.join(finalList)))
