fob = open("A-small-attempt.in",'r')
fob2 = open("Jashan.out",'w')
t = int(fob.readline())
u=1
while(t>0):
    count=0
    a=int(fob.readline())
    #print a
    b=4-a
    while(a>0):
        row=fob.readline()
        a=a-1
    while b>0:
        gar=fob.readline()
        b=b-1        
    a=map(int,row.split())
    nxt=int(fob.readline())
    b=4-nxt
    while(nxt>0):
        row=fob.readline()
        nxt=nxt-1
    while b>0:
        gar=fob.readline()
        b=b-1

    nxt=map(int,row.split())
    for i in a:
       for j in nxt:
           if i==j:
               count=count+1
               ans=i
    if count>1:
        fob2.write("Case #"+str(u)+": "+"Bad magician!"+'\n')
    elif count==0:
        fob2.write("Case #"+str(u)+": "+"Volunteer cheated!"+'\n')
    else:
        fob2.write("Case #"+str(u)+": "+str(ans)+'\n')
    u=u+1
    t=t-1
        

fob.close()
fob2.close()
