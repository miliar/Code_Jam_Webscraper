import math
import sys

sys.stdin = open("C-small-2-attempt0.in", "r")
sys.stdout = open("C-small-2.txt", "w")

def maxmin(n):
    if (n%2==0):
        return n/2, n/2-1
    return n/2,n/2

for case in xrange(int(raw_input())):
    n,k = map(int,raw_input().split())    
    level = int(math.floor(math.log(k,2)))      
    mx,mn = 0,0
    #print n,k

    if (level == int(math.floor(math.log(n,2)))):
        print "Case #"+str(case+1)+": 0 0"
        continue

    elif (level==0):
        mx,mn = maxmin(n)
        
    else:
        occ = {}
        if (n%2==0):
            occ[n/2] = 1
            occ[n/2-1] = 1
        else:
            occ[n/2] = 2

        for i in xrange(1,level):
            nocc = {}
            for key in occ:
                if (occ[key] > 0):
                    if not key/2 in nocc:
                        nocc[key/2] = 0
                    if not key/2-1 in nocc:
                        nocc[key/2-1] = 0
                    
                    if (key%2==0):
                        nocc[key/2] += occ[key]
                        nocc[key/2-1] += occ[key]
                    else:
                        nocc[key/2] += 2*occ[key]
            occ = nocc            
            #print occ  
            
        st = k - (2**(level)-1)
        for key in occ:
            if (occ[key] == 0):
                occ.pop(key, None)
                break;
        
        pos = sorted([key for key in occ])
        if (len(pos)>1):
            if (st <= occ[pos[1]]):
                mx,mn = maxmin(pos[1])
            else:
                mx,mn = maxmin(pos[0])
        else:
            mx,mn = maxmin(pos[0])

    print "Case #"+str(case+1)+": "+str(mx)+" "+str(mn)

sys.stdin.close()
sys.stdout.close()

            
    
    
        

    
