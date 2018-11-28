import sys

from collections import Counter

import copy

def process(plates, special):
    plates.sort()
    #print "delai:", special, "pancakes:", plates
    if plates[-1] == 1: 
        #print "retour: ", 1+special
        return 1+special

    lastelem = plates[-1]
    values = []
    for i in range(2,lastelem/2+1):
        newplates = plates[:-1]
        newplates.append(i)
        newplates.append(lastelem-i)
        values.append(process(newplates, special+1))
    
    values.append(process([i-1 for i in plates if (i-1)>0], special+1))
    
    #return min([lastelem+special, process(newplates,special+1)])    
    return min( values )    


if __name__=="__main__":
    T = int(sys.stdin.readline())
    for t in range(1,T+1):
        D = int(sys.stdin.readline())
        plates = [int(i) for i in sys.stdin.readline().split()]
        #print D, plates
        print "Case #%i: %i"%(t,process(plates,0))
        #print "---"