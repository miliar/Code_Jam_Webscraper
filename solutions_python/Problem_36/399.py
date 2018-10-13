import sys
from copy import copy
 
f = open('/home/moha/pre-releases/code-jam/C-small-attempt0.in', 'r')
o = open('/home/moha/pre-releases/code-jam/C-small-attempt0.out', 'w')

sr = "welcome to code jam"
n = f.readline().strip();

for i in range(int(n)):
    sentence_x = f.readline().strip();
    sentence = []
    x = 0
    for c in sentence_x:
        sentence.append((x, c))
        x+=1
        
    combo = [('',0)]
    count = 0
    
    for src in sr:
        if len(combo) == 0:
            break
        tcombo = combo[:]
        combo = []
        for e in tcombo:
            en = e[1]
            ec = e[0]
            if en > len(sentence):
                continue
            for c in sentence[en:]:
                if c[1] == src:
                    combo.append((ec+c[1], c[0]))
        tcombo = []
    
    for e in combo:
        if e[0] == sr:
            count+=1
            if count > 10000:
                count = 0
                
    o.write("Case #" + str(i+1) + ": " + "%(#)04d" % {'#': count} + "\n")
        