'''
Jirasak Chirathivat
'''
import os
import os.path
import sys
import math

sys.setrecursionlimit(1000000000)

#### CHANGE HERE ####
#globals()['happy'] = {}
filename = 'C-small-attempt1.in'

#### CHANGE HERE ####

def solve(sounds, low, high):
    for i in range(low, high+1):
#        if i in sounds:
#            continue
        found = True
        for s in sounds:
            if s % i == 0 or i % s == 0:
                pass
            else:
                found = False
                break # break the for
        if found:
            return i
    return 'NO'


if __name__ == '__main__':    
    afile = file(filename)
    aread = afile.readlines()
    afile.close()
    
    out = file('cout.txt', 'w')
    
    aread = [x.strip() for x in aread]
    
    numcase = int(aread[0])
    
    line = 1
    
    #happy = createHappy()
    
    for i in range(1, numcase + 1):
        
        #### CHANGE HERE ####
        nSounds, low, high = [int(x) for x in aread[line].split(' ')]
        sounds = [int(x) for x in aread[line+1].split(' ')]
        line += 2
        #### CHANGE HERE
        #print 3 % 1
        #print 1 % 3
        #result = process(i, caseData)
        result = solve(sounds, low, high)
        print >> out, 'Case #%s: %s' % (i,  result)
        print 'Case #%s: %s' % (i,  result)
    
    out.close()
