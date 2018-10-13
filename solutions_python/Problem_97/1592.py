a=int(input());
for i in range(1,a+1):
    b=input().split(' ')
    p=0
    for j in range(int(b[0]),int(b[1])+1):
        tar=str(j)
        x=set()
        for k in range(len(tar)-1):
            ne=int(tar[k+1:]+tar[:k+1])
            if(j<ne and ne<=int(b[1]) and ne not in x):
                p+=1
                x.add(ne)
                #print(tar+','+str(ne))
    print('Case #'+str(i)+': '+str(p))
    
