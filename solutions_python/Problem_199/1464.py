import os, sys;
# I was going to use this to match the output to the file name, but since the same
# source will be used for practice, small and large inputs I changed my mind.
#fileName = os.path.basename(__file__).split('.')[0]

fileName = 'A-large'
print 'Running problem ' + fileName
inputFile = open(fileName + '.in', 'r')
outputFile = open(fileName + '.out', 'w')

# Writes answers for each case to terminal and to output file.
def writeAnswer(case, answer):
    line = 'Case #' + str(i + 1) + ': ' + str(answer)
    print line
    outputFile.write(line + "\n")

# The first line of every program is the number of cases.
cases = int(inputFile.readline())
print str(cases) + ' cases'


for i in range(cases):
    print 'Solving case ' + str(i + 1)
    values = inputFile.readline().split()
    print values[0]
    cakes = list(values[0])
    k = int(values[1])
    possible = 1
    flips = 0
    # Solve by simulating an optimal strategy for flipping the cakes.
    for cake in range(len(cakes)):
        if cakes[cake] != '+':
            if (cake + k > len(cakes)):
                possible = 0
                break
            flips += 1
            for flipCake in range(cake, cake + k):
                cakes[flipCake] = '-' if (cakes[flipCake] == '+') else '+'
            # Uncomment this to see the state after each flip.
            # print cakes

    writeAnswer(i, flips if possible else 'IMPOSSIBLE')
