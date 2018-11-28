#!python2
'''
Created on Apr 11, 2014

@author: Mike
'''

import sys

def deceitfulWar(b, naomi, ken):
    naomi.sort()
    ken.sort()
    
    #print naomi
    #print ken
    
    nScore = 0
    
    i = 0
    while i < b:
        
        #print naomi[i]
        #print ken
        
        if (naomi[i] < ken[0]):
            ken.pop(len(ken)-1)
        else:
            ken.pop(0)
            nScore += 1
        
        i += 1
    
    return nScore




def normalWar(b, naomi, ken):
    
    naomi.sort(reverse=True)
    ken.sort(reverse=True)
    
    #print naomi
    #print ken
    
    nScore = 0
    
    i = 0
    while i < b:
        
        #print naomi[i]
        #print ken
        
        best = len(ken) - 1
        j = 0
        while j < len(ken):
            
            
            if ken[j] > naomi[i]:
                best = j
            
            j += 1
            
        #print naomi[i], ken[best]
        
        if naomi[i] > ken[best]:
            nScore += 1
        
        ken.pop(best)
            
        i += 1
    
    return nScore


def openForWriting():
    from os.path import expanduser
    home = expanduser("~")
    path = home + '/git/GoogleCodeJam2014/Qualification/' + "dw1.txt"
    
    wf = open(path, 'w')
    
    return wf

def readFile(fileName):
    import copy
    from os.path import expanduser
    home = expanduser("~")
    path = home + '/Downloads/' + fileName 
    #print path
    f = open(path , 'r')
    
    wf = openForWriting()
    
    cases = int( f.readline() )
    
    i = 1
    while i <= cases:
        blocks = int( f.readline() )
        naomi = f.readline().rstrip('\n').split(" ")
        ken = f.readline().rstrip('\n').split(" ")
        
        
        dw = deceitfulWar(blocks, copy.deepcopy(naomi), copy.deepcopy(ken))
        nw = normalWar(blocks, naomi, ken)
        
        wf.write( ("Case #" + str(i) + ": " + str(dw) + " " + str(nw) + "\n").encode('UTF-8') )
        print ("Case #" + str(i) + ": " + str(dw) + " " + str(nw) ).encode('UTF-8')
        i += 1
        

if __name__ == '__main__':
    fileName = sys.argv[-1]
    readFile(fileName)