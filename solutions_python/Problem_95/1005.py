#!/usr/bin/env python
import sys

fdict = open(sys.argv[1], 'r')

lines = fdict.readlines()
index = int(lines.pop(0))

mDict = {}

for i in range(index):
    #read data
    alien = lines.pop(0).strip()
    human = lines.pop(0).strip()
    
    #read all info
    for a in range(len(alien)):
        mDict[alien[a]] = human[a]
    
for b in mDict.keys():
    print 'key:' + b + '>' + mDict[b]
        
fdict.close()

fin = open(sys.argv[2], 'r')
fout = open(sys.argv[3], 'w')

lines = fin.readlines()
index = int(lines.pop(0))

for i in range(index):
    #read data
    alien = lines.pop(0).strip()
    
    #read all info
    fout.write('Case #' + str(i+1) + ': ')
    for a in range(len(alien)):
        fout.write(mDict[alien[a]])
    fout.write('\n')

fin.close()
fout.close()