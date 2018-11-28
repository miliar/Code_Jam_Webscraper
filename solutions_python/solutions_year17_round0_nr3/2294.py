import math
from heapq import heappush, heappop

def output (A, B):
    heap = []
    dictionary = {}
    
    heappush (heap, -1 *A) # min heap
    dictionary [A] = 1
    
    iterator = 0
    while (iterator < B):

        val = -1 *heappop (heap)
        number = dictionary [val]
        dictionary[val] = 0

        #print (val)
        #print (number)
        
        parts = split (val)

        if (parts[0] == 0 and parts[1] == 0):
            return (0, 0)
        if (iterator +number >= B):
            return parts
        
        if (parts[0] in dictionary):
            dictionary[parts[0]] += number
        else:
            dictionary[parts[0]] = number
            #print (parts[0])
            heappush (heap, -1*parts[0])

        if (parts[1] in dictionary):
            dictionary[parts[1]] += number
        else:
            dictionary[parts[1]] = number
            #print (parts[1])
            heappush (heap, -1*parts[1])
        iterator += number

    
    val = -1 *heappop (heap)
    number = dictionary [val]
    dictionary[val] = 0

    parts = split (val)
    return parts


def split (partition):
    partA = int ((partition-1)/2)
    partB = partition -1 - partA
    return (partB, partA)

    
def getInput ():
    array = []
    with open('input3.txt') as f:
        l = [int(x) for x in next(f).split()]
        i = 1
        for line in f: # read rest of lines
            array = []
            array.append([int(x) for x in line.split()])
            out = output(array[0][0], array[0][1])

            print ("Case #" +str(i) + ": " + str(out[0]) + " " + str (out[1]))

            i+=1

getInput()
