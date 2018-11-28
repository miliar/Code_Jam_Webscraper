#!/usr/bin/python
# coding: utf-8

def solve(shynessMax, distribution):
    nbFriends = 0
    nbStanding = int(distribution[0])
    nbMissingFriends = 0
    index = 1
    for i in distribution[1:]:
        if (nbStanding < index):
            nbMissingFriends = nbMissingFriends + (index - nbStanding)
            
        nbFriends = nbFriends + nbMissingFriends
        nbStanding = nbStanding + nbMissingFriends + int(i)
        nbMissingFriends = 0
        index = index + 1
        
    return nbFriends

with open('smallDataset/sample.in') as fin:
    inputData = fin.read().splitlines()
    
nbCases = inputData[0]
rspTpl = []
for i in inputData[1:]:
    iSplit = i.split(" ")
    rspTpl.append(solve(iSplit[0], iSplit[1]))

rspStr = ""
index = 1
for i in rspTpl:
    rspStr = rspStr + "Case #" + str(index) + ": " + str(i) + "\n"
    index = index + 1

with open('smallDataset/sample.out', 'w') as fout:
    fout.write(rspStr)
