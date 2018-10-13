import os, sys, math;
# I was going to use this to match the output to the file name, but since the same
# source will be used for practice, small and large inputs I changed my mind.
#fileName = os.path.basename(__file__).split('.')[0]

fileName = 'C-small-2-attempt0'
print 'Running problem ' + fileName
inputFile = open(fileName + '.in', 'r')
outputFile = open(fileName + '.out', 'w')

# Writes answers for each case to terminal and to output file.
def writeAnswer(case, answer):
    line = 'Case #' + str(case + 1) + ': ' + str(answer)
    print line
    outputFile.write(line + "\n")

# The first line of every program is the number of cases.
cases = int(inputFile.readline())
print str(cases) + ' cases'


# Put the solution logic in a function so that variables we define will be local to the solution logic.
def solveProblem():
    for case in range(cases):
        print 'Solving case ' + str(case + 1)
        line = inputFile.readline().split()
        stalls = int(line[0])
        people = int(line[1])
        # print str(stalls) + ' stalls ' + str(people) + ' people'
        lastPowerOfTwo = 2 ** int(math.floor(math.log(people, 2)))
        # print '2^x = ' + str(lastPowerOfTwo)
        remainingStalls = stalls - (lastPowerOfTwo - 1)
        # print 'remaining ' + str(remainingStalls)
        # This floating number doesn't have enough precision to give me the exact values
        # I need for minStalls/maxStalls, so I adjust them afterwards to get exact values.
        averageStalls = float(remainingStalls) / float(lastPowerOfTwo)
        # print 'average ' + str(averageStalls)
        minStalls = int(math.floor(averageStalls))
        while (minStalls * lastPowerOfTwo > remainingStalls):
            minStalls -= 1
        while ((minStalls + 1) * lastPowerOfTwo <= remainingStalls):
            minStalls += 1
        maxStalls = int(math.ceil(averageStalls))
        while (maxStalls * lastPowerOfTwo < remainingStalls):
            maxStalls += 1
        while ((minStalls - 1) * lastPowerOfTwo >= remainingStalls):
            maxStalls -= 1
        # print str(minStalls) + ' - ' + str(maxStalls)
        numberOfMaxStalls = remainingStalls - minStalls * lastPowerOfTwo
        # print 'max ' + str(numberOfMaxStalls)
        remainingPeople = people - lastPowerOfTwo
        if remainingPeople < numberOfMaxStalls:
            stalls = maxStalls
        else:
            stalls = minStalls

        # print stalls
        # print math.ceil((stalls - 1) / 2)
        # print math.floor((stalls - 1) / 2)

        # When dividing by 2, make sure we don't cast to float, otherwise we will lose precision.
        if stalls % 2: # odd number of stalls
            maxStalls = minStalls = (stalls - 1) / 2
        else: # even number of stalls
            minStalls = stalls / 2 - 1
            maxStalls = stalls / 2

        # Apparently python handles arbitrary sized ints so there is no risk of overflow here.
        # Casting to int removes leading '0's.
        writeAnswer(case, str(maxStalls) + ' ' + str(minStalls))

solveProblem()
