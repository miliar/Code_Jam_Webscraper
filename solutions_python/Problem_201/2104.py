# -*- coding: utf-8 -*-
"""
Created on Sat Apr 08 17:58:01 2017

@author: Abhishek
"""

def runMain(caseStr):
    caseStr = caseStr.split()
    n = int(caseStr[0])
    k = int(caseStr[1])
    lrs=[]
    slots=[]
    slots.append([n, 0, True])
    for i in range(k):
#        print i, len(slots), slots
        slots = sorted(slots, key=lambda x: (x[0], -x[1]))
#        print i, len(slots), slots
        nextSlot = slots.pop()
        slen = nextSlot[0]
        sidx = nextSlot[1]
#        print i, nextSlot
        if slen>1:
            if slen%2==0:
                slots.insert(0,[slen/2, sidx + slen/2, False])
                if slen/2>1:
                    slots.insert(0,[slen/2-1, sidx, True])
                lrs.insert(0, [slen/2-1, slen/2])
            else:
                slots.insert(0,[(slen-1)/2, sidx, True])
                slots.insert(0,[(slen-1)/2, sidx + (slen+1)/2, False])
                lrs.insert(0, [(slen-1)/2,(slen-1)/2])
        else:
            lrs.insert(0, [0,0])
#        print 'left right', lrs
    return lrs[0]   
        
        
        
if __name__ == "__main__":
    inputFile = 'C:\Users\Abhishek\Documents\Python Scripts\codejam\C-small-1-attempt0.in'
    outputFile = 'C:\Users\Abhishek\Documents\Python Scripts\codejam\C-small-1-attempt0.out'
    answers=[]
    with open(inputFile, 'r') as f:
        numCases = int(f.readline())
        for i in range(numCases):
            line = f.readline()
            lrs = runMain(str(line))
            answers.append(str(max(lrs))+" "+str(min(lrs)))
    with open(outputFile, 'w') as wf:
        for i in range(len(answers)):
            wf.write("Case #"+str(i+1)+": "+answers[i]+"\n")
