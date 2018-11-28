import sys

def printLine (case, result):
    print ('Case #{0}: {1}'.format(case, result))

def calculate (input):
    friends = 0
    standing = 0

    for index, item in enumerate(input):
        if (index > standing):
            added = (index - standing)
            friends += added
            standing += added
                
        standing += item
        #print ("item: {} index: {} standing: {} friends: {}".format(item, index, standing, friends))

    return friends

first = True
casenum = 1

for line in sys.stdin:
    if first:
        first = False
    else:
        input = []
        for i in range(line.index(' ')+1,len(line)-1):
            input.append(int(line[i]))
        printLine(casenum, calculate(input))
        casenum +=1

