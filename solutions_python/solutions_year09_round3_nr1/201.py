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
filename = 'a.test'
#### CHANGE HERE ####

def getbase(number):
    dlist = []
    for ec in number:
        if ec not in dlist:
            dlist.append(ec)
    return dlist, len(dlist)

def getreplace(dlist):
    rlist = []
    i = 0
    dlist2 = []
    for i in range(len(dlist)):
        if i == 0:
            rlist.append('1')
            dlist2.append(chr(2))
        if i == 1:
            rlist.append('0')
            dlist2.append(chr(1))
        if i > 1 and i < 10:
            rlist.append(str(i))
            dlist2.append(chr(i + 1))
        if i >= 10:
            rlist.append(chr(65+(i-10)))
            dlist2.append(chr(i + 1))
    return rlist, dlist2

def gettmpreplace(dlist):
    rlist = []
    i = 0
    for i in range(len(dlist)):
        rlist.append(chr(i + 1))
    return rlist

def transform(number, dlist, rlist):
    nn = number
    for i, j in zip(dlist, rlist):
        nn = nn.replace(i, j)
    return nn

def process(casenum, casedata):
    #### CHANGE HERE ####
    number = casedata[0]
    
    dlist, base = getbase(number)
    if base == 1:
        dlist.append('0')
        base = 2
    rlist, dlist2 = getreplace(dlist)
    rlist2 = gettmpreplace(dlist)
    
    # Change from dlist to rlist2
    nn = transform(number, dlist, rlist2)
    
    # Change from dlist to rlist2
    nn = transform(nn, rlist2, rlist)
    print nn
#    if nn.find('000') == 0:
#        print number, nn, rlist, dlist, base
    nn = int(nn, base)
    
    return nn
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
        number = aread[line]
        #### CHANGE HERE ####
        #### CHANGE HERE ####
        #continue
        caseData = (number,)
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
        #print 'result', result
        print >> out, 'Case #%s: %s' % (i,  result)
    
    casefile.close()
    out.close()
