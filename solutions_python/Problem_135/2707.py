fob=open('A-small-attempt2.in','r')

T=fob.readline()##no. of test cases
T=int(T)
li=[]##arrangement grid
lt=[]##comparison grid
l1=[]
la=[]##answer list
for i in range(T):
    for j in range(2):
        r=fob.readline() ##row in which card is stored
        r=int(r)
        r=r-1
        for m in range(4):
            a,b,c,d=fob.readline().split()
            a,b,c,d=int(a),int(b),int(c),int(d)
            li.append([a,b,c,d])
        lt.append(li[r])
        li=[]
    for j in range(4):
        for k in range(4):
            if(lt[0][j]==lt[1][k]):
                l1.append(lt[0][j])
    lt=[]
    l=len(l1)
    if(l==1):
        la.append(l1[0])
        l1=[]
    elif(l>1):
        la.append('Bad magician!')
        l1=[]
    elif(l==0):
        la.append('Volunteer cheated!')
        l1=[]
for i in range(T):
    print 'Case #'+str((i+1))+':',la[i]
                
fob.close()              
