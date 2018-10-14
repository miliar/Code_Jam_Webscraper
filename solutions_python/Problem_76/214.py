'''
Created on May 6, 2011

Google Code Jam

user: philipbo

@author: Phil Bozak
'''

def patSum(sett):
    summ = 0
    for aaa in sett:
        summ = summ ^ aaa
    return summ

import os
thisname = os.path.basename(__file__)
namefile = thisname.split('.')[0]

import itertools

fr = open(namefile+'.in', 'r')
fc = fr.read()
fr.close()

lines = fc.split('\n')
numCases = int(lines[0])

output = ""
for z in range(numCases):
    cands = [ int(b) for b in lines[2*z+2].split(' ') ]
    
    maxSoFar = 0
    spl = cands
    for a in range(2**len(spl)-2):
        st = bin(a+1)[2:]
        bi = [ 0 for ii in range(len(spl)-len(st))]
        for i in st:
            bi.append(int(i))
        
        set1 = []
        set2 = []
        for c in range(len(spl)):
            if bi[c]:
                set1.append(spl[c])
            else :
                set2.append(spl[c])
        p1 = patSum(set1)
        p2 = patSum(set2)
        if p1==p2:
            maxSoFar = max([maxSoFar, sum(set1), sum(set2)])
    
    if maxSoFar==0:
        maxSoFar="NO"
    
    print z    
    output = output + "Case #"+str(z+1)+": "+str(maxSoFar)+"\n"


fw = open(namefile+'.txt', 'w')
fw.write(output)
fw.close()