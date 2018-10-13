import math
def fns(p):
    f=open(p,'r')
    n=int(f.readline())
    l=[]
    for i in range(n):
        l.append(f.readline().split())
    result=pal(l)

def pal(l):
    f=open('C:/Users/raiyan/Downloads/outC','w')
    j=0
    for e in l:
        count=0
        j=j+1
        for i in range(int(e[0]),int(e[1])+1):
            
            if isPal(i)==True:
                if int(math.sqrt(i))**2==i:
                    if isPal(int(math.sqrt(i)))==True:
                        count=count+1
                        
        f.write('Case #'+str(j)+': '+str(count)+'\n')

def isPal(s):
    s=str(s)
    if s[:]==s[::-1]:
        return True
    else:
        return False


        
        
