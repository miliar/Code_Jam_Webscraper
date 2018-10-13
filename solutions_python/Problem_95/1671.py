#! /usr/bin/env python
# -*- coding:utf-8 -*-

inFile = open("input.txt","r")
outFile = open("output.txt","w")
caseNum = 0
readNum = 0

letterMap = {
      " ":" "
    }

def completeMap():
    letters = "abcdefghijklmnopqrstuvwxyz"    
    keys = letterMap.keys()

    noneKey = []
    # which letter is not exist in Google?
    for l in letters:
        if letterMap.has_key(l) == False:
            noneKey.append(l)
    # which letter is not exist in English?
    noneMap = []
    for l in letters:
        bFound = False
        for key in keys:
            if letterMap[key] == l:
                bFound = True
        if bFound == False:
            noneMap.append(l)
    for i in range(len(noneMap)):
        letterMap[noneKey[i]] = noneMap[i]
    
def createLetterMap(g,e):
    for i in range(len(g)):
        if letterMap.has_key(g[i]) == False:
            letterMap[g[i]] = e[i]
    
def translate(g):
    e = ""
    for i in range(len(g)):
        if letterMap.has_key(g[i]) == True:
            e = e + letterMap[g[i]]
    return e

def googlerese(case,line):
    g = line
    e = translate(g)
    print "Case #%d: %s" % (case,e)
    return  "Case #%d: %s\n" % (case,e)


if __name__ == "__main__":

    for line in inFile.readlines():
        readNum = readNum + 1
        if readNum == 1:
            items = line.split()
            caseNum = int(items[0])
            continue
        
        createLetterMap("y qee ","a zoo")
        createLetterMap("ejp mysljylc kd kxveddknmc re jsicpdrysi","our language is impossible to understand")
        createLetterMap("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd","there are twenty six factorial possibilities")
        createLetterMap("de kr kd eoya kw aej tysr re ujdr lkgc jv","so it is okay if you want to just give up")

        completeMap()
        outFile.write(googlerese(readNum-1,line))

