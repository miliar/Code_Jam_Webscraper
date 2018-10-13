'''
Created on 07/05/2011

@author: joan
'''

import sys

if __name__ == '__main__':
    #Read the code
    #infile = open("minimagica.txt") 
    infile = sys.stdin
    ncases = int(infile.readline())
    #print ncases
    
    for case in range(ncases):
        # Read 
        elem = infile.readline().split()
        
        ncomb = int(elem.pop(0))
        
        dcombs ={}
        for combs in range(ncomb):
            c = elem.pop(0)
            dcombs[(c[0],c[1])]= c[2]
        
        nopos = int(elem.pop(0))
        
        dopos ={}
        for oposs in range(nopos):
            o = elem.pop(0)
            
            if o[0] not in dopos:
               dopos[o[0]] = [o[1]]
            else:
               dopos[o[0]].append(o[1])   
            
            if o[1] not in dopos:
               dopos[o[1]] = [o[0]]
            else:
               dopos[o[1]].append(o[0])
        # Read sequence invocation
        
        nsimb = elem.pop(0)
        simbs = elem.pop(0)
        # Check readfile
#        print ncomb,
#        
#        for comb in dcombs:
#            print comb, dcombs[comb],
#        
#        for opos in dopos:
#            print opos, dopos[opos],
#            
#        print simbs
        res = []
        for i in range(len(simbs)):
             deleted = False
             simb = simbs[i]

                 
                 #Look substituion
             if len(res) == 0:
                res.append(simb)
                continue
                          
             sub = (res[-1],simb)
             sub2 = (simb,res[-1])
             if sub in dcombs:
                 #simb = res[-1]
                 res[-1] = dcombs[sub]
                 #res.pop()
                 continue
             elif sub2 in dcombs:
                 #res[-1] = dcombs[sub2]
                 res[-1] = dcombs[sub2]
                 #res.pop()                 
                 continue
         #Look for oposition
         #get the list for possible oposition
             opossimbs=[]
             if simb in dopos:
                 opossimbs = dopos[simb]
         
         #We found an oposible simbol
         
         #if len(opossimbs) > 0:
             #for j in range(len(res)-1,-1,-1):
             #    if res[j] in opossimbs:
    
             res.append(simb) 
             for osimb in opossimbs:
                if osimb in res:   
                    res = [] 
                    
                    break
          
                       
        
        #print res
        #print "Case #"+(case+1)+": ["+', '.join(res)+"]"
        print "Case #%d: [%s]" % ( case+1, ', '.join(res))
    
        