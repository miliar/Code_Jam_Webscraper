linestring = open('lawn', 'r').readlines()
f = open('paradoteo','w')
print (linestring)
T=int(linestring[0])
a=1
for s in range(T):
    flage=0
    bla=linestring[a].split() 
    M=int(bla[1])
    N=int(bla[0])
    print (M,N)
    pinakas=[]
    for smthn in range(1,N+1):
        pinakas.append(linestring[a+smthn].split())
    print (pinakas)
    place=[]
    flage=0
    then=0
    for i in range(N):
        for j in range(M):
           if pinakas[i][j]==str(1):
               place.append([i,j])
    if len(place)==0:
        then=1
    print (place)
    for i in place:
        x=i[0]
        y=i[1]
        i=0
        j=0
        flago=0
        for i in range(M):
            if pinakas[x][i]=='1':
                flago+=1
        flagk=0
        for j in range(N):
            if pinakas[j][y]=='1':
                flagk+=1
        if(flagk==N or flago==M):
            flage+=1
        print (flagk,flago,flage)
    if (flage==len(place)):
        f.write('Case #{}: YES'.format(s+1)+'\n')
    else:
         f.write('Case #{}: NO'.format(s+1)+'\n')
    a=a+N+1
f.close()
