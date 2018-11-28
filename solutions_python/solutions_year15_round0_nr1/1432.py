T=int(input())
i=0
while i<T:
    Sa=input()
    Sa=Sa.split(' ')
    smax=int(Sa[0])
    aud=[int(k) for k in list(Sa[1])]
    psmax=aud[smax-1]
    j=1
    suma=aud[0]
    inv=0
    while suma<smax and j<=smax:
        if suma<j and aud[j]!=0:
            dif=j-suma
            inv=inv+dif
            suma=suma+inv+aud[j]
        else:
            suma=suma+aud[j]
        j=j+1
    if smax==0:
        if aud[0]==0:
            inv=1
    print('Case #'+str(i+1)+': '+str(inv))
    i=i+1
