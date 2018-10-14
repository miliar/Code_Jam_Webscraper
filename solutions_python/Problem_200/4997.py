import sys

t=int(input())
for i in range(t):
    x=int(input())
    
    while(x>0):
        s=str(x)
        flag=0
        for k in range(len(s)-1):
                if(s[k]<=s[k+1]):
                    
                    continue
                else:
                    
                    flag=1
                    break
        
        if(flag==1):
            x=x-1
            continue
        else:
            
            print"case #{}: {}".format(i+1,x)

            break
               
