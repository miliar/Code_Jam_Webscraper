'''
Created on Sep 3, 2009

@author: Robin
'''
import string

def checkword(w, d):
    #print "checking word",w,"in",d
    for li in range(len(w)):
        if not w[li] in d[li]:
            return False
    return True

words = []
cases = []
    
f=open('b.in', 'r')
[l, d, n] = [int(x) for x in string.split(f.readline())]
for y in range(d):
    words.append(f.readline()[:-1])
for y in range(n):
    line = f.readline()
    if line[-1] == "\n":
        line = line[:-1]
    d = []
    nextBracket = string.find(line, '(')
    while nextBracket != -1:
        if (nextBracket > 0):
            d += [l for l in line[0:nextBracket]]
        d.append(line[nextBracket+1:string.find(line,')')])
        line = line[string.find(line,')')+1:]
        nextBracket = string.find(line, '(')
    if (line != ''):
         d += [l for l in line]
    c = 0
    for w in words:
        if checkword(w, d):
            c+= 1
    
    print "Case #"+str(y+1)+":",c
