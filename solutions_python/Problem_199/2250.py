t=int(raw_input())
for j in range(0,t):
    pan,k=raw_input().split(' ')
    k=int(k)
    pan=list(pan)
    count=0
    n=len(pan)
    flag=0
    for i in range(0,n):
        if(pan[i]=='+'):
            continue
        elif (pan[i]=='-' and i<=n-k):
            temp=i+k
            while(i<temp):
                if(pan[i]=='-'):
                    pan[i]='+'
                else:
                    pan[i]='-'
                i+=1
            count+=1
        elif (pan[i]=='-'):
            flag=1
            break
    if(flag==0):
        print "Case #"+str(j+1)+": "+str(count)
    else:
        print "Case #"+str(j+1)+": IMPOSSIBLE"
    
            
