INPUT_FILE = r'C:\Downloads\FromFirefox\D-large.in'
OUTPUT_FILE = r'C:\Users\Assaf\Fun\codeJam\D-large.out'

from math import factorial as fact
from random import shuffle

inputFile = file(INPUT_FILE, 'rb')
numQuestions = int(inputFile.readline())
outputFile = file(OUTPUT_FILE, 'wb')

def findCycles(l):
    undone = set(l)
    result = []
    while undone:
        start = undone.pop()
        pos = start
        cycle = [pos]
        while l[pos] != start:
            pos = l[pos]
            cycle.append(pos)
            undone.remove(pos)
        result.append(cycle)
    return result

# Just for testing
def goroSort(n):
    steps = 0
    l = range(n)
    shuffle(l)
    cycles = findCycles(l)
    for cycle in cycles:
        if len(cycle) > 1:
            steps += 1
            steps += goroSort(len(cycle))
    return steps

def solveQuestion(numbers):
    cycles = findCycles(numbers)
    total = 0
    for cycle in cycles:
        if len(cycle) > 1:
            total += len(cycle)
    
    return '%d.000000' % total

for q in xrange(numQuestions):
    outputFile.write("Case #%d: " % (q+1))
    l = int(inputFile.readline())
    numbers = map(int, inputFile.readline().split(' '))
    numbers = map(lambda x:x-1, numbers)
    if len(numbers) != l:
        raise Exception("Input error N")
    result = solveQuestion(numbers)
    outputFile.write(result)
    outputFile.write("\n")

outputFile.close()
inputFile.close()
# print file(OUTPUT_FILE, 'rb').read()
