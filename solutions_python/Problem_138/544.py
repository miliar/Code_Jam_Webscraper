from string import *

def read_words(filename):
    '''
    converts a file to a list
    '''
    
    words = []
    for line in filename:
            words.append(line.strip())
    return words


def normal(ktemp, ntemp, numblocks):
    kwins = 0
    nwins = 0
    for kblock in range(numblocks):
        for nblock in range(numblocks):
            if (ktemp[kblock]>ntemp[nblock]):
                #ken wins a game
                #print "wtf"
                kwins+=1
                #remove ktemp[kblock], ntemp[nblock]
                ktemp[kblock] = 0
                ntemp[nblock] = 1.1 #effectively removes these guys
            
    nwins = numblocks-kwins
                #print "wins: "+ str(nwins)
    return nwins

def deceitful(ktemp2, ntemp2, numblocks):
    #print ktemp2
    #print ntemp2
    
    # Deceitful Game
  
    cheatwins = 0

    while (len(ntemp2)>0):
        #print ntemp2
        if (ntemp2[0]>ktemp2[0]):
            #print str(ntemp2[0]) + "beats" + str(ktemp2[0])
            cheatwins+=1 # Naomi tricks Ken by declaring her smallest as greater than Ken's greatest
            del ntemp2[0]
            del ktemp2[0]
        else:
            #Naomi tells ken her smallest is just smaller than ken' biggest. Ken wastes his biggest.
            del ntemp2[0]
            del ktemp2[-1]
            
    return cheatwins


filename = open("naomi.txt", 'r')
numcases = int(filename.readline())

for cases in range (numcases):
    numblocks = int(filename.readline())
    
    naomi = filename.readline().split()
    ken = filename.readline().split()
    
    for i in range (numblocks):
        naomi[i] = float(naomi[i])
        ken[i] = float(ken[i])
    
    naomi = sorted(naomi)
    ken = sorted(ken)    
    #print naomi
    #print ken
    naomi2 = []
    ken2 =[]
    for p in range(numblocks):
        naomi2.append(naomi[p])
        ken2.append(ken[p])
    #print "Number of blocks: " + str(numblocks)
    #print ken2
    #print naomi2
    print "Case #" + str(cases+1) + ": "  + str(deceitful(ken2, naomi2, numblocks)) + ' ' +str(normal(ken, naomi, numblocks))
            
             
    
       
    
    
    
    