#!/usr/bin/python
import os, sys

f = open("/Users/maxallen/Desktop/Projects/Python/Google Code Jam/A-small-attempt2.in",'r')
#f = open("/Users/maxallen/Desktop/Projects/Python/Google Code Jam/input.txt",'r')
o = open("/Users/maxallen/Desktop/Projects/Python/Google Code Jam/output.txt",'w')

numTestCases = int(f.readline())
for i in range(numTestCases):
    line = f.readline()
    Smax = int(line[0]) + 1
    numPeopleStanding = 0
    peopleNeeded = 0
    line = line[2:]
    if line[-1] == '\n':
        line = line[:-1]
    for j in range(len(line)):
        x = int(line[j])
        #print "Index: " + str(j)
        #print "Peple at index: " + str(x)
        #print "People Standing: " + str(numPeopleStanding)
        #print "Sufficient People Standing: " + str(numPeopleStanding >= j)
        if numPeopleStanding >= j:
            # There's enough people standing for this index (j)
            numPeopleStanding += x
        else:
            # There's not enough people standing for this index
            # There should be j-numPeopleStanding more people
            pN = (j-numPeopleStanding)
            peopleNeeded += pN
            #print "People needed: " + str(peopleNeeded)
            numPeopleStanding += x + pN
        #print 
    
    if i == numTestCases -1:
        o.write("Case #" + str(i+1) + ": " + str(peopleNeeded))
    else:
        o.write("Case #" + str(i+1) + ": " + str(peopleNeeded)+"\n")

print "Done!"
f.close()