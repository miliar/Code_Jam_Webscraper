#import os
#print os.path.dirname(os.path.realpath(__file__))

def totalPeople(string):
    assert string.isdigit()
    total = 0
    for dig in string:
        total += int(dig)
    return total

def operaOvation(inputFile, outputFile):
    outputFile = open(outputFile, 'w')
    inputFile = open(inputFile, 'r').read()
    inputList = inputFile.splitlines()
    inputList.pop(0)
    isFirst = True
    for case in xrange(len(inputList)):
        if isFirst:
            isFirst = False
        else:
            outputFile.write('\n')
        outputFile.write('Case #' + str(case + 1) +': ')
        string = inputList[case]
        index = string.index(" ")
        string = string[index + 1:]
        standing, added = 0, 0
        for shyLevel in xrange(len(string)):
            while shyLevel > standing:
                standing += 1
                added += 1
            standing += int(string[shyLevel])
        outputFile.write(str(added))

operaOvation('attempt-large.txt', 'result-large.txt')

