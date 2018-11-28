#! /usr/bin/env python
# -*- coding:utf-8 -*-

inFile = open("input.txt","r")
outFile = open("output.txt","w")
caseNum = 0
readNum = 0

def googlers(case,line):
    column = line.split()
    dancerNum = int(column[0])
    surpNum = int(column[1])
    threshold = int(column[2])
    answer = 0

    if threshold >= 2:
        minNormal = threshold + (threshold - 1) * 2
        minSurp =  threshold + (threshold - 2) * 2
    if threshold == 1:
        minNormal = 1
        minSurp = 1
    if threshold == 0:
        minNormal = 0
        minSurp = 0
    
    scores = []
    for idx in range(3,len(column)):
        scores.append(int(column[idx]))

    for score in scores:
        #Normal
        if score >= minNormal:
            answer = answer + 1
            continue
        
        #Surprising
        if surpNum > 0:
            if score >= minSurp:
                answer = answer + 1
                surpNum = surpNum - 1

    print "Case #%d: %d" % (case,answer)
    return  "Case #%d: %d\n" % (case,answer)


if __name__ == "__main__":

    for line in inFile.readlines():
        readNum = readNum + 1
        if readNum == 1:
            items = line.split()
            caseNum = int(items[0])
            continue
        outFile.write(googlers(readNum-1,line))



    
