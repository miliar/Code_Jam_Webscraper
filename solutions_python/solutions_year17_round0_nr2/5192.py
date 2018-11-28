def isTidy(x):
    t1=x
    d1=t1%10
    t1//=10
    while(t1!=0):
        d2=t1%10
        t1//=10
        if(d1>=d2):
            d1=d2
        else:
            return False
    return True
        

t=int(input())
li=[]
for i in range(t):
    li.append(int(input().strip()))
c=0
for i in li:
    c+=1
    while(not isTidy(i)):
        i-=1
    print("case #{0}: {1}".format(c,i))
    
