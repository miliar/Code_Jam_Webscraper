'''
Jirasak Chirathivat
'''
import psyco
psyco.full()

import os
import os.path
import sys
sys.setrecursionlimit(1000000000)
#### CHANGE HERE ####
globals()['happy'] = {}
globals()['happy2'] = {}
filename = 'a.test'
#### CHANGE HERE ####

def create(nl):
    result = []
#    print nl
    if len(nl) == 1:
        return [nl]
    for i in range(len(nl)):
        #print nl[i], nl[0:i] + nl[i+1:]
        insideList = create(nl[0:i] + nl[i+1:])
        for elist in insideList:
            result.append([nl[i]] + elist)
    #print result
    return result

def toint(x):
    result = 0
    for i in x:
        result += i
        result *= 10
    return result / 10

def transzero(n, index):
    nl = []
    i = n
    while i:
        nl.insert(0, i % 10)
        i /= 10
    nl.insert(index, 0)
    print nl 
    return toint(nl)

def process(casenum, casedata):
    #### CHANGE HERE ####
    n = casedata[0]
    i = n
    nl = []
    
    while i:
        nl.append(i % 10)
        i /= 10
    nl2 = create(nl)
    for x in range(len(nl2)):
        nl2[x] = toint(nl2[x])
    nl2 = set(nl2)
    nl2 = sorted([x for x in nl2])
    
    if nl2.index(n) + 1 == len(nl2):
        i = 1
        index = 1
        while True:
            for j in nl2:
                print j, n
                newval = transzero(j, index)
                print newval
                if newval > n:
                    return newval
                nl2.append(newval)
                nl2.sort()
            index += 1
            
    
    #print n, nl2
    print n, nl2[nl2.index(n) + 1] 
    return nl2[nl2.index(n) + 1]
        
#    return i
    #### CHANGE HERE ####

if __name__ == '__main__':
    afile = file(filename)
    aread = afile.readlines()
    afile.close()
    
    out = file('out.txt', 'w')
    casefile = file('casefile.txt', 'w')
    
    aread = [x.strip() for x in aread]
    
    numcase = int(aread[0])
    
    line = 1
    
    for i in range(1, numcase + 1):
        
        #### CHANGE HERE ####
        n = int(aread[line])
        #### CHANGE HERE ####
        
        #### CHANGE HERE ####
        caseData = (n, )
        tomove = 1
        #### CHANGE HERE ####

        if False:
            print >> casefile, 'Case #%s' % i
            print >> casefile, '%s\n' % '\n'.join(aread[line: line + tomove])
            print >> casefile, '%s\n\n\n' % ('\n'.join([str(x) for x in caseData]))
        
        #### CHANGE HERE ####
        line += tomove
        #### CHANGE HERE
        result = process(i, caseData)
        print 'result', result
        print >> out, 'Case #%s: %s' % (i,  result)
    
    casefile.close()
    out.close()
