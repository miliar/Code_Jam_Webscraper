import math
from decimal import *

f = open ('A-large.in', 'r');

def getLine(splitter=" "):
    return tuple(z for z in f.readline()[:-1].split())

def getInts():
    return tuple(int(z) for z in f.readline().split())

##new code below this line

def main():
    getcontext().prec = 40
    (N, K) = getInts()
    pancakes = [getLine() for i in range(N)]
    stack = []
    top = 0
    side = 0
    for p in range(K):
        mx = 0
        for i in range(len(pancakes)):
            added = max((Decimal(pancakes[i][0])**Decimal(2))*Decimal(math.pi) - top, Decimal(0)) + Decimal(2)*Decimal(math.pi)*Decimal(pancakes[i][0])*Decimal(pancakes[i][1])
            if (added > mx):
                mx = added
                sol = i;
        top += max((Decimal(pancakes[sol][0])**Decimal(2))*Decimal(math.pi) - top, Decimal(0))
        side += Decimal(2)*Decimal(math.pi)*Decimal(pancakes[sol][0])*Decimal(pancakes[sol][1])
        pancakes.pop(sol)

    result = top + side
    
    #print(result)
    return result;

##newcode above this line

output = "";
(cases,) = getInts();
for case in range(1, cases+1):
    output += "Case #" + str(case) + ": ";
    output += str(main());
    output += "\n";

with open('A-large.out', 'w') as o:
    o.write(output)
