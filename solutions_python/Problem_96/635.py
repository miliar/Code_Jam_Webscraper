# Paul Johnson
# GCJ 2012 Problem B

from sys import *

def spread(l):
    l.sort()
    return l[2]-l[0]

input = open(argv[1], 'r')
output = open(argv[2],'w')

testCases = int(input.readline())

for x in range(testCases):
    case = input.readline().split()
    numOfGoogs = int(case[0])
    surprises = int(case[1])
    minScore = int(case[2])
    l = case[3:]
    gglers = []
    for y in l: gglers.append(int(y))
    poss = 0
    surp = 0
    minPoss = 3*minScore-2
    minSurp = 3*minScore-4
    for y in gglers:
        if minScore < 2:
            if y >= minScore: poss += 1
        elif y >= minPoss: poss += 1
        elif y >= minSurp and surp < surprises: surp += 1

    

    output.write("Case #%i: %i\n"%(x+1,poss+surp))

output.close()
input.close()