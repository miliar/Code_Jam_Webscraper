import sys
import math

def ResString(s):
    if s == '':
        return "[]"
    ret = "["
    for c in s:
        ret += c + ", " 
    return ret[:-2] + ']'


count = 1
for line in sys.stdin.readlines()[1:]:
    entries = line.strip().split(' ')
    
    combs = int(entries[0])
    combines = list()
    for i in range(1, combs+1):
        combines.append(entries[i])

    opps = int(entries[combs+1])
    opposes = list()
    for i in range(combs+2, combs+2+opps):
        opposes.append(entries[i])

    elements = entries[-1]

    #print combines, opposes, elements
    
    eList = ""

    for c in elements:
        eList = eList + c
        
        if len(eList) < 2:
            continue

        combined = False
        for c in combines:
            if(eList[-1] == c[0] and eList[-2] == c[1]) or (eList[-2] == c[0] and eList[-1] == c[1]):
                eList = eList[:-2] + c[2]
                combined = True
                break
        
        if not combined:
            for o in opposes:
                if o[0] == o[1]:
                    if eList.count(o[0]) > 1:
                        eList = ""
                        break
                else:
                    if eList.count(o[0]) > 0 and eList.count(o[1]) > 0:
                        eList = ""
                        break
            
        

    #print eList


    print "Case #" + str(count) + ": " + ResString(eList)
    count += 1 
