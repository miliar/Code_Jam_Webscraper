import math
def call(a,b):
    c=math.log(2*b,2)
    c=int(c)
    ma=0
    mi=0
    count=0
    flag=0
    for i in range(1,c+1,1):
        ma=(a//pow(2,i))
        mi=(a//pow(2,i-1)-a//pow(2,i)-1)
        if ma==mi:
            count+=pow(2,i-1)
            flag=pow(2,i-1)
    if count>0:        
        if(int(math.log(b,2))==int(math.log(flag,2))):
            count-=flag
    if(b<=(pow(2,c-1)+count) or b==pow(2,c-1)):
        return int(ma),int(mi)
    else:
        if ma>mi:
            return int(ma)-1,int(mi)
        else:
            return int(ma),int(mi)-1
            
    
n=int(input())
for k in range(n):
    x,y=input().split(' ')
    x,y=[int(x),int(y)]
    z,w=call(x,y)
    print('Case #'+str(k+1)+': '+str(z)+' '+str(w))
