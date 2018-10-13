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
filename = 'A-large.in'

#### CHANGE HERE ####

def solve(N, Pd, Pg):
    i = 1
    while i < N+1:
        if i * Pd % 100 == 0:
            gamesWon = (i * Pd) / 100
            x = i
            gamesLost = i - gamesWon
            if Pd != 0 and Pg == 0:
                return 'Broken'
            if Pd != 100 and Pg == 100:
                return 'Broken'
            return 'Possible'
        i += 1
    return 'Broken'

def solve2(N, Pd, Pg):
    for i in range(1, N+1):
        if i * Pd % 100 == 0:
            gamesWon = (i * Pd) / 100
            x = i
            gamesLost = i - gamesWon
            if Pd != 0 and Pg == 0:
                return 'Broken'
            if Pd != 0 and Pg == 0:
                return 'Broken'
            while 1: # Increment total game one by one 
                allSmaller = True
                for y in range(gamesWon, (x-gamesLost)+1): # y is the number of gamesWon
                    percent = (y * 100.00) / x
                    #print percent, Pg
                    if abs(percent - Pg) <= 0.00000001:
                        return 'Possible'
                    if percent > Pg:
                        allSmaller = False
                if allSmaller:
                    return 'Broken'
                x += 1
    return 'Broken'

if __name__ == '__main__':    
    afile = file(filename)
    aread = afile.readlines()
    afile.close()
    
    out = file('out.txt', 'w')
    
    aread = [x.strip() for x in aread]
    
    numcase = int(aread[0])
    
    line = 1
    
    #happy = createHappy()
    
    for i in range(1, numcase + 1):
        
        #### CHANGE HERE ####
        case = aread[line]
        N, Pd, Pg = [int(x) for x in case.split(' ')]
        line += 1
        #### CHANGE HERE

        #result = process(i, caseData)
        result = solve(N, Pd, Pg)
        print >> out, 'Case #%s: %s' % (i,  result)
        print 'Case #%s: %s' % (i,  result)
    
    out.close()
