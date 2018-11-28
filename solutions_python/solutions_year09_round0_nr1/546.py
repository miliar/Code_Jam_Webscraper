#!/usr/bin/env python
import re
f = open('A-large.in','r')
lines2 = []
lines = f.xreadlines()
for line in lines:
    line = line.splitlines()[0]
    line = line.replace('(','[')
    line = line.replace(')',']')
    lines2.append(line)
del lines

firstLine = lines2[0]
l1 = firstLine.split(" ")
len1 = int(l1[1])
len2 = int(l1[2])

line1s = lines2[1:len1+1]
line2s = lines2[len1+1:]
del lines2
f.close()

patternList = []

for item in line2s:
    patternList.append(re.compile(item)) 
    
index = 0
countList = []
for item in patternList:
    countList.append(0)
    for line in line1s:
        m = item.match(line)
        if m:
            countList[index] += 1
    index += 1

index = 1    
for item in countList:
    print "Case #%d: %d" % (index,item)
    index += 1