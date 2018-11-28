import math
def isPal(num):
    a=num
    rev=0
    while(a>0):
        rev=rev*10+a%10
        a=a/10
    if rev==num:
        return True
    return False

inp=open('C-small-attempt0.in','r')
n=int(inp.readline().rstrip('\n'))
for counter in range(1,n+1):
    limits=inp.readline().rstrip('\n').split(' ')
    low=int(limits[0])
    up=int(limits[1])
    l=int(math.sqrt(low))
    u=int(math.sqrt(up))
    j=0
    for i in range(l,u+1):
        if isPal(i**2) and isPal(i):
            if i**2>=low:
                j+=1
    print 'Case #%d: %d'%(counter,j)

   
            
    


