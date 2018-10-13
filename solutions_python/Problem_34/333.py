import sys
import math
import decimal
import copy
import re


class Solver:
    def __init__(self, input, output):
#        size = int(input.readline())
#        print (str(size))
#        for index in range(size):
        numbers = [int(part) for part in input.readline().strip().split()]
        amountOfWords = numbers[1];
        characterAmount = numbers[0];
        amountOfTestcases = numbers[2];
        self.words = []
        for i in range(amountOfWords):
            self.words.append(input.readline().strip());
        for i in range(amountOfTestcases):
            result = self.solve(input.readline().strip())
            print ("Case #" + str(i + 1) + ": " + str(result))
            output.write("Case #" + str(i + 1) + ": " + str(result) + "\n")
    def solve(self, regex):
        regex = regex.replace('(', '[')
        regex = regex.replace(')', ']')
        result = 0;
        for word in self.words:
            if (re.match(regex,word)):
                result+=1
        return result
        
class ACase:
    def __init__(self, file):
        numbers = [int(part) for part in file.readline().strip().split()]
        self.P = numbers[0]
        self.K = numbers[1]
        self.L = numbers[2]
        self.frequencies = [int(part) for part in file.readline().strip().split()]
    def solve(self):
        solution = 0
        self.frequencies.sort()
        self.frequencies = self.frequencies[::-1]
        for i, frequency in enumerate(self.frequencies):
            solution += frequency * int(1 + i/self.K)
        return str(solution)         
        
type = "A"
if (0):
    size = "-small-attempt1" 
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

