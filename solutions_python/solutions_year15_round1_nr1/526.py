# Google Code Jam 2015 Qualifying 1A.
import sys

# How many splits does it take to convert num pancakes into stacks
# not taller than target?
def countSplits(num, target):
    if num <= 1:
        return 0
    # We do (9,3) by removing 3 twice (making 3 stacks of 3).
    return (num - 1) / target


def doCase(file):
    file.readline()             # Ignore number of intervals
    sizes = map(int, file.readline().split())
    eaten1 = 0
    maxeaten = 0
    for i in range(len(sizes) - 1):
        eaten = sizes[i] - sizes[i+1]
        if eaten > 0:
            eaten1 += eaten 
            maxeaten = max(maxeaten, eaten)
    rate = maxeaten
    eaten2 = 0
    for i in range(len(sizes) - 1):
        eaten2 += min(rate, sizes[i])

    return "{0} {1}".format(eaten1, eaten2)

def run():
    file = open(sys.argv[1])
    numCases = int(file.readline())
    for case in range(1, numCases+1):
        answer = doCase(file)
        print 'Case #{0}: {1}'.format(case, answer)
run()
