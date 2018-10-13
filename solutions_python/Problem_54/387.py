###############################
def GCD(x,y):

    while(y):
        x=x%y
        x,y=y,x

    return x;

#################################
C= raw_input()
C=int(C)

for i in range(C):
    str = raw_input()

    itemList =str.split()

    N = itemList.pop(0)
    N = int(N)
    time = []

    for item in itemList:
        time.append(int(item))
    
    time.sort()

    D=[]
    for k in range(N-1):
        temp=time[k+1]-time[k]
        if(temp!=0):
            D.append(temp)


    if(len(D)>1):
        mod = GCD(D[0],D[1])
    
        for j in range(len(D)-2):
            mod = GCD(mod,D[j+2])
    
    if(len(D)==1):
        mod = D[0]
    if(len(D)==0):
        mod = time[0]

    ans = (mod-time[0]%mod)%mod
    print "Case #%d: %d"%(i+1,ans)

