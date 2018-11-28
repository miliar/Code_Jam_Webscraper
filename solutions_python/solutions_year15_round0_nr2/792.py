import sys
sys.setrecursionlimit(5000)
import copy 

from math import sqrt

n = int(input())


def alg(plates):
                
    p1 = [(x-1 if x > 0 else 0) for x in plates]
    ok = True
    for x in plates:
        if x != 0:
            ok = False
            break
    
    if ok == False:
        d1 = 1+alg(p1)

        
        

        
        di = d1
            
        for k in range(2,1+int(sqrt(plates[0]))):
            i=0
            while plates[i] % k != 0 :
                i += 1
                if i == len(plates):
                    break
                        
           

            if i < len(plates) and plates[i] != 0:
                pi = copy.deepcopy(plates)
                    
                    
                pi.append(plates[i]//k)
                pi[i] = plates[i]-plates[i] // k
                
                di = min(di,1+alg(sorted(pi,reverse=True)))
                   
           
           
        return di
    else:
        return 0

for i in range(n):
    nd = int(input())
    data = [int(x) for x in input().split()]
    
    print ("Case #",i+1,": ",alg(sorted(data,reverse=True)),sep="")
