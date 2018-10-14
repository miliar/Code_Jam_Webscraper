o=open('output.txt','w')
a=open('D-large.txt')
T=int(a.readline())
for xt in range(1,T+1):
    N=int(a.readline())
    nao=a.readline()
    Naomi=[float(x) for x in nao.split()]
    ke=a.readline()
    Ken=[float(x) for x in ke.split()]
    for j in range(0,N-1):
        for k in range(0,N-1-j):
            if Naomi[k]>Naomi[k+1]:
                Naomi[k],Naomi[k+1]=Naomi[k+1],Naomi[k]
            if Ken[k]>Ken[k+1]:
                Ken[k],Ken[k+1]=Ken[k+1],Ken[k]


    #Arranged In Ascending Order
    i=0
    j=0
    count1=0
    while i<N and j<N:
        if Naomi[i]>Ken[j]:
            i+=1
            j+=1
            count1+=1
        else:
            i+=1

    i=0
    j=0
    count2=0
    while i<N and j<N:
        if Ken[i]>Naomi[j]:
            i+=1
            j+=1
        else:
            count2+=1
            i+=1
    o.write("Case #"+`xt`+": "+`count1`+" "+`count2`+"\n")
