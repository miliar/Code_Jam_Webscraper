#!/usr/bin/python

import math

def Mirror(number):
        for digit in range(int(len(number)/2)):
                if number[digit] != number[len(number)-1-digit]:
                        return False
        return True;
        

try:
        with open("C-small-attempt0.in") as inFile, open("output.txt", "w") as outFile:
                cases = int(inFile.readline().strip())
                for c in range(cases):
                        combos = 0
                        rangeArray = inFile.readline().split(" ")
                        small = int(rangeArray[0].strip())
                        large = int(rangeArray[1].strip())
                        smallRoot = int(math.sqrt(small))
                        largeRoot = int(math.sqrt(large))
                        for each in range(smallRoot, largeRoot+1):
                                if Mirror(str(each)) == True:
                                        square = str(each * each)
                                        if int(square) >= small and int(square) <= large:
                                                if Mirror(square) == True:
                                                        combos = combos + 1
                        outFile.write("Case #" + str(c+1) + ": " + str(combos) + "\n")
except IOError as err:
        print(str(err))
