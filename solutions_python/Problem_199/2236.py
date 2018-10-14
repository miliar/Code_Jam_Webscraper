t=input()
tt=t

while t>0:
    a=raw_input().split()
    b=list(a[0])
    k=int(a[1])
    flag=0
    flag2=0

    c=[]
    count=0
    for x in b:
        if x=='+':
            c.append(0)
        else:
            c.append(1)
    if sum(c)==0:
        flag=1
       
    while sum(c)!=0 and flag2==0:
        
        i=c.index(1)
        count=count+1
        x=0
        if i+k-1<=len(c)-1:
            while x<k:
            
               if c[i]==0:
                 c[i]=1
               else:
                 c[i]=0
            
               i=i+1
               x=x+1
        else:
            flag2=1
    
            
    
    if flag==1:
        print 'Case #'+str(tt-t+1)+':'+' '+str(0)
    elif sum(c)!=0 or flag2==1:
        print 'Case #'+str(tt-t+1)+':'+' '+'IMPOSSIBLE'
    else:
        print 'Case #'+str(tt-t+1)+':'+' '+str(count)
        
        
        
    
    t=t-1
    
       
            
        
            
