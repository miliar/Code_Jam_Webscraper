import os
import sys
import re

f = file("d:\\a.txt")

l = f.readline()
l = l.split(" ")
wordlen = int(l[0])
cwords = int(l[1])
cases = int(l[2])
words = []

def findinlist(L,f):
    for i in L:
        if i == f:
            return True
    return False    
    

def solve(c,word):
    word = word.replace('(','[').replace(')',']')
    cc = 0
    for ww in words:
        p = re.findall(word,ww)
        cc = cc + len(p)
        
    print "Case #" + str(c) + ": " + str(cc)
            
            

for i in range(0,cwords):
    words.append(f.readline()[0:wordlen])
    
for i in range(0,cases):
    w = f.readline()
    solve(i+1,w[0:len(w)-1])

f.close()
