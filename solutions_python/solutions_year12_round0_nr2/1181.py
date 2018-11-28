f=open("dance.txt")
n=f.readline()
n=int(n)
for index in range(1,n+1):
    lis=[]
    temp=f.readline()
    li=temp.split(' ')
    n=int(li[0])
    s=int(li[1])
    p=int(li[2])
    for pl in range(3,n+2):
        ti=int(li[pl])
        lis=lis+[[ti,0,0]]
    last=int(li[n+2].split('\n')[0])
    lis=lis+[[last,0,0]]
    for i in range(p,11):
        it1=i-2
        it2=i+3
        if(it1<0):
            it1=0
        for j in range(it1,it2):
            for k in range(it1,it2):
                if((abs(i-j)>2)|(abs(i-k)>2)|(abs(j-k)>2)):
                    break
                elif((abs(i-j)==2)|(abs(i-k)==2)|(abs(j-k)==2)):
                    if(s<=0):
                        continue
                    else:
                        te=i+j+k
                        for q in range(0,n):
                            if(te==lis[q][0]):
                                if(s<=0|lis[q][2]):
                                    break
                                else:
                                    s=s-1
                                    lis[q][2]=1
                                    lis[q][1]=lis[q][1]+1
                else:
                     te=i+j+k
                     for q in range(0,n):
                        if(te==lis[q][0]):
                            lis[q][1]=lis[q][1]+1
    calc=0            
    for lca in range(0,n):
        if(lis[lca][1]):
            calc=calc+1
    print"Case #"+str(index)+": "+str(calc)
