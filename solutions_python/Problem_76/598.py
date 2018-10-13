'''
Created on May 7, 2011

@author: jirasak
'''
import itertools

def removeAll(allCandies, seans):
    patrick = allCandies * 1
    for s in seans:
        patrick.remove(s)
    return tuple(patrick)

def xsum(candies):
    sumC = 0
    for c in candies:
        sumC = sumC ^ c
    return sumC

def xequal(seans, patrick):
    if xsum(seans) == xsum(patrick):
        return True
    return False

if __name__ == '__main__':
    fIn = file('C-small-attempt1.in')
    inLines = fIn.readlines()
    fIn.close()
    
    inLines = inLines[1:]
    numLines = len(inLines)
    i = 0
    tc = 0
    while i < numLines:
        line = [int(x) for x in inLines[i+1].strip().split(' ')]
        print 'Case #%d:' % (tc+1),
        maxS = -1
        
#        perms = []
#        for j in range(len(line)/2):
#            permObject = itertools.combinations(line, j)
#            while True:
#                try:
#                    perms.append(permObject.next())
#                except:
#                    break
        
        for j in range(len(line)):
            permObject = itertools.combinations(line, j)
            while True: 
                try:
                    seans = permObject.next()
                    patrick = removeAll(line, seans)
                    if xequal(seans, patrick):
                        maxS = max(maxS, sum(seans))
                except:
                    break
        if maxS < 0:
            print 'NO'
        else:
            print maxS
        
        
        i += 2
        tc += 1
        #print line