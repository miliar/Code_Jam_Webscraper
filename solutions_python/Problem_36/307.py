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
            case = CCase(input)
            result = case.solve()
            print ("Case #" + str(index + 1) + ": " + str(result))
            output.write("Case #" + str(index + 1) + ": " + str(result) + "\n")
        
class CCase:
    def __init__(self, file):
        self.line = file.readline().strip();
    def solve(self):
        toTest = "welcome to code jam"
        previous = []
        previous.append(PA(-1,1))
        for char in toTest:
            previous = self.getNextAmounts(char, previous)
        result = 0
        for pa in previous:
            result = (result + pa.amount)% 10000
        return str(result).zfill(4)

    def getNextAmounts(self, char, previous):
        if (len(previous) < 1):
            return [];
        currentIndex = self.line.find(char, previous[0].position + 1)
        total = previous[0].amount
        index = 1
        result = [];
        while currentIndex != -1:
            while (index < len(previous) and previous[index].position < currentIndex):
                total = (previous[index].amount + total) % 10000
                index+=1
            result.append(PA(currentIndex, total))
            currentIndex = self.line.find(char, currentIndex + 1)
        return result;
class PA:
   def __init__(self, position, amount):    
        self.position = position
        self.amount = amount
        
type = "C"
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

