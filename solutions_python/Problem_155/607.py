#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def calculate(shyness):
    countShyness = 0
    countIndex = 0
    countNeedPeople = 0
    for x in shyness:
        if countShyness + countNeedPeople < countIndex:
            countNeedPeople += 1
            #print "in if"
        #print "countShyness : " + str(countShyness)
        #print "countIndex : " + str(countIndex)
        #print "countNeedPeople : " + str(countNeedPeople)
        #print x
        countShyness += int(x)
        #print "countNeedPeople : " + str(countNeedPeople)
        countIndex += 1
    
    return countNeedPeople
    #print "countNeedPeople : " + str(countNeedPeople)

f = open("A-large.in", "r")

caseCount = int(f.readline())
for x in range(0, caseCount):
    readline = f.readline()
    shynessMax = readline.split(" ")[0]
    shyness = readline.split(" ")[1].strip()
    #print shyness
    print "Case #" + str(x+1) + ": " + str(calculate(shyness))

#calculate("110011")