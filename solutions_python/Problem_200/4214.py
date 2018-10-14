def listdig(num):
    return [int(i) for i in str(num)]
    
    
    
def change(alist,dig):
    n=0
    flag=True
    count=0
    while(flag and n<dig):
        
        if(alist[n]>alist[n+1]):
            if(count==0):
               alist[n]=(alist[n]+9)%10
               count=1
            for i in range(dig-n):
               alist[n+i+1]=9
               flag=False 
          
        n=n+1
        
                       
    return alist
    
    
    
def check(alist,dig):
    while(dig>0):
        if(alist[dig]<alist[dig-1]):
            return(True)
        else:
            dig=dig-1
    return(False)    
    
    
    
t=int(raw_input()) 
for i in range(t):    
    
    n=int(raw_input())
    
    flag=True
    new=listdig(n)
    dig=len(new)
    while(flag==True):
       new=change(new,dig-1)
       flag=check(new,dig-1)
       num=reduce(lambda a,b:a*10+b,new)
    print("Case #%d: %d" %(i+1,num))   
