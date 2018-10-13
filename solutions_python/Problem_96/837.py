'''
Created on May 6, 2011

Google Code Jam

user: philipbo

@author: Phil Bozak
'''

def gtP(n,p):
    if n==0:
        return n>=p
    l = n / 3
    r = n % 3
    if r==0:
        if l>=p:
            return True
        else:
            return False
    else:
        if (l+1)>=p:
            return True
        else:
            return False
        
def gtP2(n,p):
    l = n / 3
    r = n % 3
    if n==0:
        return (r)>=p
    if r==0:
        if (l+1)>=p:
            return True
        else:
            return False
    elif r==2:
        if (l+2)>=p:
            return True
        else:
            return False
    else: #r==1
        if (l+1)>=p:
            return True
        else:
            return False

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
    nums = lines[casenum].split(' ')
    N = int(nums[0])
    S = int(nums[1])
    p = int(nums[2])
    ngtp = 0
    googlers = []
    for i in range(N):
        googlers.append(int(nums[3+i]))
    nextgooglers = googlers[:]
    for g in googlers:
        if gtP(g,p):
            ngtp += 1
            nextgooglers.remove(g)
            print str(g)+"     yes"
    print nextgooglers
    for ng in nextgooglers:
        if S==0:
            break
        if gtP2(ng,p):
            ngtp += 1
            S = S - 1
            print str(ng)+"     yes"
        else:
            print str(ng)+"     no"
    output += "Case #"+str(casenum)+": "+str(ngtp)+"\n"
    
output=output[:-1]
fw = open(namefile+'.txt', 'w')
fw.write(output)
fw.close()