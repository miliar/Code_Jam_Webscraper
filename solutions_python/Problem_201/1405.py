import sys
import datetime
import heapq

def runBathroomStalls(input):
    numStalls = int(input[0])
    people = int(input[1])
    # list of stalls will always be in descending order, with first number being largest
    listOfStalls = MaxHeap()
    left = 0
    right = 0
    for i in range(people):
        if not listOfStalls:
            currentLargestStalls = numStalls
        else:
            currentLargestStalls = listOfStalls.heappop()
        if currentLargestStalls % 2 == 0:
            left = currentLargestStalls / 2
            right = currentLargestStalls / 2 - 1
        else:
            left = (currentLargestStalls - 1) / 2
            right = (currentLargestStalls - 1) / 2
        addToStalls(listOfStalls, left, right)
    return '%s %s' % (int(max(left, right)), int(min(left, right)))


def addToStalls(listOfStalls, left, right):
    # leftInserted = False
    # rightInserted = False
    # for i in range(0, len(listOfStalls)):
    #     currentValue = listOfStalls[i]
    #     if leftInserted and rightInserted:
    #         break
    #     if left > right:
    #         if not leftInserted and left >= currentValue:
    #             listOfStalls.insert(i, left)
    #             leftInserted = True
    #         if not rightInserted and right >= currentValue:
    #             listOfStalls.insert(i + 1, right)
    #             rightInserted = True
    #     else:
    #         if not rightInserted and right >= currentValue:
    #             listOfStalls.insert(i + 1, right)
    #             rightInserted = True
    #         if not leftInserted and left >= currentValue:
    #             listOfStalls.insert(i, left)
    #             leftInserted = True
    # if not leftInserted:
    #     listOfStalls.append(left)
    # if not rightInserted:
    #     listOfStalls.append(right)
    # return listOfStalls
    listOfStalls.heappush(left)
    listOfStalls.heappush(right)


class MinHeap(object):
    def __init__(self): self.h = []

    def heappush(self, x): heapq.heappush(self.h, x)

    def heappop(self): return heapq.heappop(self.h)

    def __getitem__(self, i): return self.h[i]

    def __len__(self): return len(self.h)


class MaxHeap(MinHeap):
    def heappush(self, x): heapq.heappush(self.h, x * -1)

    def heappop(self): return heapq.heappop(self.h) * - 1

    def __getitem__(self, i): return self.h[i].val


inputFile = open('bathroomStalls.input', 'r')

outputFile = open('bathroomStalls.output', 'w')

numLines = int(inputFile.readline())

print (datetime.datetime.now())

for i in range(0, numLines):
    num = inputFile.readline()
    input = num.split(" ")
    outputFile.write('%s%s%s%s\n' % ('Case #', (i + 1), ': ', runBathroomStalls(input)))

    print (i)

print (datetime.datetime.now())