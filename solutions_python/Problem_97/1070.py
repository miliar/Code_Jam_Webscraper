import itertools
'''
Created on May 6, 2011

@author: jirasak
'''

def getCycles(num):
    cycleSet = set()
    strings = str(num)
    for i in range(len(strings)):
        cycleNumber = int(strings[i:] + strings[:i])
        cycleSet.add(cycleNumber)
    return cycleSet

def solve(i, aMin, aMax):
    count = 0
    numSet = set()
    for i in range(aMin, aMax+1):
        if(i not in numSet):
            cycles = getCycles(i)
            if len(cycles) > 1:
                for permute in itertools.combinations(cycles, 2):
                    a = permute[0]
                    b = permute[1]
                    if a >= aMin and a <= aMax and b >= aMin and b <= aMax:
                        count += 1
                        numSet.add(a)
                        numSet.add(b)
#                for c in cycles:
#                    if c >= aMin and c <= aMax:
#                        count += 1
    return count

if __name__ == '__main__':
    fIn = file('C-small-attempt0.in')
    inLines = fIn.readlines()
    fIn.close()
    
    inLines = inLines[1:]
    numLines = len(inLines)
    i = 0
    while i < numLines:
        line = inLines[i].strip()
        i += 1
        aMin = int(line.split(' ')[0])
        aMax = int(line.split(' ')[1])
        data = solve(i, aMin, aMax)
        print 'Case #%s: %s' % (i, data)
    