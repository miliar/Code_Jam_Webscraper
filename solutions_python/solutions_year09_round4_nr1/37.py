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

class CCase:
    def __init__(self, file):
        temp = [int(part) for part in file.readline().strip().split()]
        self.amountOfPrisoners = temp[0];
        self.amountReleased = temp[1];
        self.released = [int(part) for part in file.readline().strip().split()]
    def solve(self):
        if (len(self.released) == 0):
            return str(0)
        return str(self.getCosts([], self.released));
    def getCosts(self, releasedBefore, toBeReleased):
        costs = []
        for prisoner in self.minifyToBeReleased(toBeReleased, releasedBefore):
            costs.append(self.calculateCosts(prisoner, releasedBefore, toBeReleased))
        return min(costs)
    def calculateCosts(self, prisonerToRelease, releasedBefore, toBeReleased):
        min = 0;
        max = self.amountOfPrisoners + 1;
        for i in releasedBefore:
            if (i < prisonerToRelease and i > min):
                min = i
            if (i > prisonerToRelease and i < max):
                max = i
        toBeAdded = max - min - 2
        toBeReleasedNew=toBeReleased[:]
        releasedBeforeNew=releasedBefore[:]
        toBeReleasedNew.remove(prisonerToRelease)
        releasedBeforeNew.append(prisonerToRelease)
        if (len(toBeReleasedNew) == 0):
            return toBeAdded
        return self.getCosts(releasedBeforeNew, toBeReleasedNew) + toBeAdded
    def minifyToBeReleased(self, toBeReleased, releasedBefore):
        return toBeReleased
               
class BCase:
    def __init__(self, file):
        self.amountOfPoints = int(file.readline())
        self.points = []
        for i in range(self.amountOfPoints):
            self.points.append([int(part) for part in file.readline().strip().split()])
    def solve(self):
        current = [0,0,0,0,0,0]
        for i in self.points:
            for j in range(len(i)):
                current[j] = current[j] + i[j];
        for j in range(len(i)):
            current[j]/=self.amountOfPoints
        if ((current[3]*current[3] + current[4]*current[4] + current[5]*current[5] )> 0):
            t = -(2*current[0]*current[3] + 2*current[1]*current[4] + 2*current[2]*current[5])/(2*(current[3]*current[3] + current[4]*current[4] + current[5]*current[5]))
        else:
            t = 0;
        if (t < 0):
            t = 0;
        d = math.sqrt(math.pow(current[0]+current[3]*t, 2) + math.pow(current[1]+current[4]*t, 2) + math.pow(current[2]+current[5]*t, 2))
        return str(d) + " " + str(t);
class ACase:
    def __init__(self, file):
        amountOfLines= int(input.readline())
        self.values = [];
        for i in range(amountOfLines):
            self.values.append(input.readline().strip().rfind("1"))
    def solve(self):
        total = 0;   
        while (True):
            k = -1;
            toSwitchTo = -1;
            for (i, value) in enumerate(self.values):
                if i < value and (k == -1):
                    k = i;
                else:
                    if (k != -1 and value <= k):
                        toSwitchTo = i;
                        break;
            if (k == -1):
                break;
            self.values.insert(k, self.values[toSwitchTo])
            self.values.pop(toSwitchTo + 1)
            total += toSwitchTo - k
        return total;


        
                
                
        
type = "A"
if (0):
    size = "-small-" 
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

