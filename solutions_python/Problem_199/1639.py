t=int(input())
i=1
while i<=t:
    y=input()
    y=y.split()
    y[0]=list(y[0])
    ind=0
    acc=0
    K=int(y[1])
    long=len(y[0])
    flag=True
    while ind+K<=long:
        if y[0][ind]=='-':
            acc+=1
            j=1
            while ind+j<ind+K:
                if y[0][ind+j]=='-':
                    y[0][ind+j]='+'
                else:
                    y[0][ind+j]='-'
                j+=1
        ind+=1
    while ind<long:
        if y[0][ind]=='-':
            flag=False
        ind+=1
    if flag:
        print ("Case #"+str(i)+": "+str(acc))
    else:
        print("Case #"+str(i)+": "+"IMPOSSIBLE")
    i+=1
