import sys
import os, stat
import itertools

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
    numRows = 2;
    count = 0
    for i in range(numCases):
        firstLine = input.readline().rstrip('\n')
        secondLine = input.readline().rstrip('\n')
        #numRows = int(firstLine.partition(' ')[0])
        #numCols = int(firstLine.partition(' ')[2])
        # lines = [input.readline().rstrip('\n') for j in range(numRows)]

        [n, p] = [int(num) for num in firstLine.split(' ')]
        sizes = [int(num) for num in secondLine.split(' ')]

        count += numRows + 1

        #print 'Case #%d:\n%s'%(i+1, '\n'.join(evaluate(lines, numRows, numCols)))
        print 'Case #%d: %s'%(i+1, evaluate(n, p, sizes))
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

def divUp(a, b):
    return a/b + (1 if a%b != 0 else 0)

def evaluate(n, p, groups):
    if p == 1:
        return n
    if p == 2:
        return evaluateP2(n, groups)
    if p == 3:
        return evaluateP3(n, groups)

def evaluateP2(n, groups):
    count0 = 0
    count1 = 0
    for group in groups:
        if group%2 == 0:
            count0 += 1
        else:
            count1 += 1
    return count0 + count1/2 + (1 if count1%2 != 0 else 0)

def evaluateP3(n, groups):
    count0 = 0
    count1 = 0
    count2 = 0
    for group in groups:
        if group%3 == 0:
            count0 += 1
        elif group%3 == 1:
            count1 += 1
        else:
            count2 += 1
    count = count0
    if count1 < count2:
        count += count1
        count += (count2-count1)/3 + (1 if (count2-count1)%3 != 0 else 0)
    else:
        count += count2
        count += (count1-count2)/3 + (1 if (count1-count2)%3 != 0 else 0)
    return count

main()

