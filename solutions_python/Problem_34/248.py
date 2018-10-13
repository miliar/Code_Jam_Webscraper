'''
Jirasak Chirathivat
'''

import os
import os.path
import sys
sys.setrecursionlimit(1000000000)

#### CHANGE HERE ####
filename = 'A-small-attempt0.in'
#### CHANGE HERE ####


def transform(pattern):
    a = False
    newpat = []
    for eachchar in pattern:
        if eachchar == '(':
            smalllist = []
            a = True
            continue
        if eachchar == ')':
            a = False
            newpat.append(smalllist)
            continue
        if a:
            smalllist.append(eachchar)
        else:
            newpat.append(eachchar)
    return newpat

def process(casenum, casedata):
    #### CHANGE HERE ####
    numlettes, words, pattern = casedata
    
    newpattern = transform(pattern)
    
    count = 0
    for eachword in words:
        found = True
        for eachchar, eachpat in zip(eachword, newpattern):
            if eachchar not in eachpat:
                found = False
                break
        if found: 
            count +=1 
    
    #print count
    return count
    #### CHANGE HERE ####

if __name__ == '__main__':
    afile = file(filename)
    aread = afile.readlines()
    afile.close()
    
    out = file('out.txt', 'w')
    casefile = file('casefile.txt', 'w')
    
    aread = [x.strip() for x in aread]
    
    numcase = int(aread[0].split(' ')[2])
    
    # special 
    numletters = int(aread[0].split(' ')[0])
    numwords = int(aread[0].split(' ')[1]) 
    words = aread[1: 1 + numwords]
    
    line = 1 + numwords
    for i in range(1, numcase + 1):
        
        #### CHANGE HERE ####
        pattern = aread[line]
        #### CHANGE HERE ####
        
        #### CHANGE HERE ####
        caseData = (numletters, words, pattern )
        tomove = 1
        #### CHANGE HERE ####

        if False:
            print >> casefile, 'Case #%s' % i
            print >> casefile, '%s\n' % '\n'.join(aread[line: line + tomove])
            print >> casefile, '%s\n\n\n' % ('\n'.join([str(x) for x in caseData]))
        
        #### CHANGE HERE ####
        line += tomove
        #### CHANGE HERE
        
        print >> out, 'Case #%s: %d' % (i,  process(i, caseData))
    
    casefile.close()
    out.close()
    #os.startfile('out.txt')
    #os.startfile('casefile.txt')  
