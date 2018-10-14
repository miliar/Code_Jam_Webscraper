import sys
import math
# print("Case #{}: {} {}".format(i, n + m, n * m))

sys.stdin  = open("incs.in")
sys.stdout = open("ocs.out","w")

def val(m):
    if m%2!=0 :
        out1,out2 = [m//2, m//2]
    else :
        out1,out2 = [m//2, (m//2)-1]
    return [out1,out2]



n = int(input())
for i in range(n) :
    line = input().split(' ')
    #print(line)
    line = [int(x) for x in line]
    m,k = line
    liste = []
    pat = 1
    p = 0
    
    if k==m :
        out=[0,0]
    elif k!=1 :
        
        
    
        #while(True):
            #try :
             #   ind = int(liste.index(pat))  
              #  break;
            #except :
        se = m;
        #for iu in range(int(math.log(se,2))+1):
        while(True):
                if m%2!=0 :
                    liste.extend([m//2,m//2])
                else :
                    liste.extend([m//2 -1,m//2])
                liste.sort()
                liste.reverse()
                m = liste[p]
                if(m==1):
                    break
                p = p + 1
        
        #print(liste) 
        out = val(liste[k-2])
    else :
        out = val(m)
            
    print("Case #",i+1,":",sep='',end=' ')
    
    print(out[0],out[1])
    
