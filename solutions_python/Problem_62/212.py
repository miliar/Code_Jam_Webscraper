#!/usr/bin/python

import sys

def main():
    numOfCases = input()
    for currentCase in range(1, numOfCases + 1):
        
        numOfWires = input()

        lWindow = []
        rWindow = []

        numOfIntersections = 0
        
        for currentWire in range(numOfWires):
            wires = raw_input().split()
            lWindow.append(int(wires[0]))
            rWindow.append(int(wires[1]))

        for i in range(len(lWindow)):
            for j in range (i, len(lWindow)):
                if (lWindow[j] > lWindow[i]) and (rWindow[j] < rWindow[i]):
                    numOfIntersections = numOfIntersections + 1
                if (lWindow[j] < lWindow[i]) and (rWindow[j] > rWindow[i]):
                    numOfIntersections = numOfIntersections + 1

        print 'Case #%d: %d' % (currentCase, numOfIntersections)
        
        


if __name__ == '__main__':
    main()
