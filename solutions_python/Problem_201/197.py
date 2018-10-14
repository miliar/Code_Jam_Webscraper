import sys
import math
from sortedcontainers import SortedList


def main():
    inputFile = open(sys.argv[1], "r")
    numCases = int(inputFile.readline())
    for n in range(1,numCases+1):
        numStalls, numPeople = inputFile.readline().split(" ")
        numStalls, numPeople = int(numStalls), int(numPeople)

        spaceToPeople = {numStalls:1}
        spaces = SortedList()
        spaces.add(numStalls)
        numEntered = 0
        largestSpace = numStalls
        while (numEntered<numPeople):
            largestSpace = spaces.pop()
            newEntered = spaceToPeople[largestSpace]
            numEntered += newEntered
            if (numEntered<numPeople):
                y = largestSpace//2
                if (largestSpace%2==0 and largestSpace!=0):
                    z = y-1
                else:
                    z = y
                if y in spaces:
                    spaceToPeople[y] += newEntered
                else:
                    spaces.add(y)
                    spaceToPeople[y] = newEntered
                if z in spaces:
                    spaceToPeople[z] += newEntered
                else:
                    spaces.add(z)
                    spaceToPeople[z] = newEntered
        y = largestSpace//2
        if (largestSpace%2==0 and largestSpace!=0):
            z = y-1
        else:
            z = y
        print("Case #%i: %i %i"%(n,y,z))


main()