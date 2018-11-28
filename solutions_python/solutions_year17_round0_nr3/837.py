inputF = open('C-large.in', 'r')
output = open('C-large.out', 'w')

import heapq

class MyQueue:
    def __init__(self):
        self.negkeyheap = []
        self.counts = {}

    def add(self, openingSize, numOpenings):
        if openingSize not in self.counts:
            self.counts[openingSize] = numOpenings
            heapq.heappush(self.negkeyheap, -1*openingSize)
        else:
            self.counts[openingSize] += numOpenings

    def getNextOpeningSize(self):
        openingSize = heapq.heappop(self.negkeyheap)*-1
        return (openingSize, self.counts[openingSize])

def enterStalls(numStalls, numPeople):
    ''' Bit better, using heapq. Should work for n = 10^6, but not large '''
    openings = MyQueue()
    openings.add(numStalls, 1)
    peopleRemaining = numPeople
    while peopleRemaining > 0:
        (openingSize, numOpenings) = openings.getNextOpeningSize()
        newLeft = (openingSize-1)/2
        newRight = openingSize/2
        openings.add(newLeft, numOpenings)
        openings.add(newRight, numOpenings)
        peopleRemaining -= numOpenings
    return (newRight, newLeft)

numCases = int(inputF.readline())

for i in range(numCases):
    line = inputF.readline().split()
    numStalls = int(line[0])
    numPeople = int(line[1])
    
    (left, right) = enterStalls(numStalls, numPeople)

    output.write('Case #' + str(i+1) + ': ')
    output.write(str(left) + ' ' + str(right) + '\n')

inputF.close()
output.close()
