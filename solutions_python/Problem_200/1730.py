def verify(x):
    flag=0
    for k in range(1,len(x),1):
            if x[k-1]>x[k]:
                flag=1
                break
    if flag==0:
        return 1
    else:
        return 0

n=int(input())
for i in range(n):
    t=int(input())
    while(True):
        val=verify(str(t))
        if val==1:
            print('Case #'+str((i+1))+': '+str(t))
            break
        else:
            y=str(t)
            for j in range(len(y)-1,-1,-1):
                if y[j]!='9':
                    z=int(y[j-1])-1
                    if z!=-1:
                        y=y[0:j-1]+str(z)+'9'+y[j+1:]
                    else:
                        y=y[0:j]+'9'+y[j+1:]
                    break
            t=int(y)
                    