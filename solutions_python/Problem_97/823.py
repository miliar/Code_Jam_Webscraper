'''
Created on Apr 13, 2012

@author: Phil
'''

def rr1(s):
    return s[-1]+s[:-1]

import os
thisname = os.path.basename(__file__)
namefile = thisname.split('.')[0] #filename (without the extension)

fr = open(namefile+'.in', 'r')
fc = fr.read()
fr.close()

lines = fc.split('\n')
output = ""
numCases = int(lines[0])

for casenum in range(1,numCases+1):
    A = int(lines[casenum].split(' ')[0])
    B = int(lines[casenum].split(' ')[1])
    c = 0
    print "======== A="+str(A)+"  B="+str(B)+"  ======\n"
    for n in range(A,B):
        d = True
        for i in range(1,len(str(n))):
            d = d and list(str(n))[0]>list(str(n))[i]
        if d:
            continue #there is no m such that m>n
        st = str(n)
        setns = set([])
        for j in range(len(str(n))):
            st = rr1(st)
            if int(st)>n and int(st)<=B:
                setns.add(int(st))
        c += len(setns)
    output += "Case #"+str(casenum)+": "+str(c)+"\n"
    
output=output[:-1]
fw = open(namefile+'.txt', 'w')
fw.write(output)
fw.close()