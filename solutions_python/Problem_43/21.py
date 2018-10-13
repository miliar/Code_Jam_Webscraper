import sys
import math
import decimal
import copy
import re


class Solver:
    def __init__(self, input, output):
        size = int(input.readline())
        print (str(size))
        for index in range(size):
            case = ACase(input)
            result = case.solve()
            print ("Case #" + str(index + 1) + ": " + str(result))
            output.write("Case #" + str(index + 1) + ": " + str(result) + "\n")       
class ACase:
    def __init__(self, file):
        self.letters= input.readline().strip();
    def solve(self):
        solution = 0
        nextIndex = 1
        indexedLetters = {}
        for letter in self.letters:
            if (letter in indexedLetters):
                continue
            else:
                indexedLetters[letter] = nextIndex
                if (nextIndex == 1):
                    nextIndex = 0
                else: 
                    if (nextIndex == 0):
                        nextIndex = 2
                    else:
                        nextIndex+=1
        if (nextIndex == 0):
            nextIndex = 2
        for letter in self.letters:
            solution = solution * nextIndex + indexedLetters[letter]
        return str(solution)         
        
type = "A"
if (0):
    size = "-small-attempt2" 
else: 
    size = "-large"
filename = "..\\" + type + size + ".in"
outputname = "result.txt"
input = open(filename, 'r')
output = open(outputname, 'w')
try:
    Solver(input, output)
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
finally:
    input.close()
    output.close()

