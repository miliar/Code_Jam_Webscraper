'''
Created on 07/05/2011

@author: joan
'''

import sys
if __name__ == '__main__':
    #Read the code
    #infile = open("minitrust.txt") 
    infile = sys.stdin
    ncases = int(infile.readline())
    #print ncases
    
    # reading data    
    for case in range(ncases):
        elem = infile.readline().split()
        
        npos = int(elem.pop(0))
        
        
        ordO = []
        ordB = []
        for i in range(npos):
            robot = elem.pop(0)
            if robot == 'O':
                 ordO.append([i,int(elem.pop(0))])
            elif robot == 'B':
                 ordB.append([i,int(elem.pop(0))])
                 
        #print ordO, ordB     

        robOpos = 1
        robBpos = 1
#                      
        finish = False
        total = 0
        while not finish:
            if len(ordO) == 0 and len(ordB) == 0:
                finish = True
                
            elif len(ordO) > 0 and len(ordB) > 0:
                if ordO[0][0] < ordB[0][0]:
                    """ Next is Orange """
                    robOswitch = ordO.pop(0)[1]
                    
                    duration = abs(robOswitch-robOpos)+1
                    robOpos=robOswitch   
                    total += duration
#                   
                    """ Compute the Blue new position """
                    robBswitch = ordB[0][1]
                    
                    if robBswitch > robBpos:
                       robBpos = min (robBswitch,robBpos+duration)
                    elif robBswitch < robBpos:
                       robBpos = max (robBswitch,robBpos-duration)
                
                elif ordB[0][0] < ordO[0][0]:
                    """ Next is Blue """
                    robBswitch = ordB.pop(0)[1]
                    
                    duration = abs(robBswitch-robBpos)+1
                    robBpos=robBswitch   
                    total += duration
#                   
                    """ Compute the Orange new position """
                    robOswitch = ordO[0][1]
                    
                    if robOswitch > robOpos:
                       robOpos = min (robOswitch,robOpos+duration)
                    elif robOswitch < robOpos:
                       robOpos = max (robOswitch,robOpos-duration)
            
            elif len(ordO) == 0:
                 for (ind,pos) in ordB:
                     total += abs(pos-robBpos)+1
                     robBpos = pos
                 finish = True
            elif len(ordB) == 0:
                 for (ind,pos) in ordO:
                     total += abs(pos-robOpos)+1
                     robOpos = pos
                 finish = True
                       
           
        print "Case #%d: %d" % ( case+1, total)         
#        cost = 0
#        
#        #For O robot take the selection
#        if arobot == 'O':
#           robOpos = switch
#           time = abs(switch-robOpos)+1  
#           
#           #check Brobot next point
#           Bswitch = 
#           
#        
#        