from sys import stdin, stdout
import math
from itertools import combinations

def calcP(lijst):
    total = 0
    for i in lijst:
        total = total ^ i
    return total

def calcS(lijst):
    return sum(lijst)

def main():
    t = int(stdin.readline())
    for i in range(1, t+1):
        n = int(stdin.readline())
        lineproc = stdin.readline().split()
        lijst = []
        for x in range(n):
            lijst.append(int(lineproc[x]))
        if n == 2:
            if lijst[0] == lijst[1]:
                print("Case #", i, ": ", lijst[0], sep ="")
            else:
                print("Case #", i, ": ", "NO", sep ="")
        else:
            for x in range(1,math.ceil(n/2)):
                output = -1
                for comb in combinations(lijst, x):
                    complement = []
                    to_delete = []
                    to_delete.extend(comb)
                    for entry in lijst:
                        if (entry in to_delete):
                            to_delete.remove(entry)
                        else:
                            complement.append(entry)
                    if (calcP(comb) == calcP(complement)) and calcS(complement) > output:
                        output = calcS(complement)
                if output != -1:
                    break
            print("Case #", i, ": ", output if output != -1 else "NO", sep ="")
                
            
        

main()
