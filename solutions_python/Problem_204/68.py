import sys
import os, stat

def main():
    mode = os.fstat(0).st_mode
    input = None
    if stat.S_ISFIFO(mode):
        #print "stdin is piped"
        input = open("input.txt")
    elif stat.S_ISREG(mode):
        #print "stdin is redirected"
        input = sys.stdin
    else:
        #print "stdin is terminal"
        input = open("input.txt")

    numCases = int(input.readline().rstrip('\n'))
    count = 0
    for i in range(numCases):
        firstLine = input.readline().rstrip('\n')
        numIngredients = int(firstLine.split(' ')[0])
        numPackages = int(firstLine.split(' ')[1])
        count += 1
        secondLine = input.readline().rstrip('\n')
        portions = [int(num) for num in secondLine.split(' ')]
        count += 1
        ingPackages = []
        for j in range(numIngredients):
            line = input.readline().rstrip('\n')
            packages = [int(num) for num in line.split(' ')]
            packages.sort()
            ingPackages.append(packages)
            count += 1
        print 'Case #%d: %s'%(i+1, str(evaluate(portions, ingPackages, numIngredients, numPackages)))
        # if (count == 0):
        #     print '\n'
        # lines = [input.readline().rstrip('\n') for j in range(numRows)]
        # print 'Case #%d:\n%s'%(i+1, '\n'.join(evaluate(lines, numRows, numCols)))
    # numLines = int(input.readline())
    # lines = [input.readline().rstrip('\n') for i in range(numLines)]
    # for (i,line) in enumerate(lines):
    #     print 'Case #%d: %s'%(i+1, str(evaluate(line)))

def csplit(line, separator):
    for part in line.split(separator):
        try:
            yield int(part)
        except:
            yield str(part)

def evaluate(portions, ingPackages, numIngredients, numPackages):
    ingIndexes = [0]*numIngredients
    numKits = 0
    while True:
        min_ingredient = -1
        max_ingredient = -1
        minServings = 10e6
        maxServings = 0
        for i in range(numIngredients):
            if (ingIndexes[i] >= numPackages):
                return numKits
            servings = ingPackages[i][ingIndexes[i]]/float(portions[i])
            if servings > maxServings:
                maxServings = servings
                max_ingredient = i
            if servings < minServings:
                minServings = servings
                min_ingredient = i
        if (maxServings <= int(minServings * 10 / 9) * float(11) / 10):
            numKits += 1
            ingIndexes = [index + 1 for index in ingIndexes]
        else:
            ingIndexes[min_ingredient] += 1


main()

