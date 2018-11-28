'''
Created on 3 Sep 2009

@author: Maksims Rebrovs
'''
data = open("A-large.in")
line = data.readline()
L,D,N = map(int,line.split(" "))
allwords = []
for i in range(D):
    allwords.append(data.readline().replace("\n",""))
patterns = []
for i in range(N):
    patterns.append(data.readline().replace("\n",""))
    
def toList(p):
    res = []
    lmnt = []
    bl = 0
    for i in range(len(p)):
        if p[i] == "(": 
            bl +=1
            if (len(lmnt)>0):
                res.append(lmnt)
                lmnt = []
        elif p[i] == ")":
            bl -=1
            if bl == 0:
                res.append(lmnt)
                lmnt = []
        else:
            if bl == 0:
                res.append(p[i])
            else:
                lmnt.append(p[i])

    if len(lmnt)>0: res.append(lmnt)
    return res
        
def matchCount(p):
    psetline = toList(p)
    print psetline

toRE = lambda p : p.replace("(", "[").replace(")", "]")

import re

for i in range(N):
    count = 0
    reg = toRE(patterns[i])
    print "Case #"+ str(i+1)+ ": "+str(len(filter(lambda x : re.match(reg, x) != None, allwords)))