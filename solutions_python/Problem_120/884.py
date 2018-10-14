from __future__ import division
from math import pi

FILE_NAME = 'A-small-attempt2.txt'



testCases = []
with open(FILE_NAME,'r') as file:
    numCases = int(file.readline())
    for lines in file:
        a,b = lines.split()
        testCases.append((int(a),int(b)))


def paintRequired(radius):
    
    area = radius**2*pi
    area -= (radius-1)**2*pi
    return round(area/pi) #Millilitres required
    
    

def Bullseye(case):
    initialRadius,millilitres = case
    currentRadius = initialRadius + 1
    blackRings = 0
    while True:
        paint = paintRequired(currentRadius)
        if paint <= millilitres:
            blackRings += 1
            millilitres -= paint
            currentRadius += 2
        else:
            return blackRings


caseNum = 1
with open('results.txt','w') as file:
    for e in testCases:
        file.write('Case #{}: {}\n'.format(caseNum,Bullseye(e)))
        caseNum += 1



    

