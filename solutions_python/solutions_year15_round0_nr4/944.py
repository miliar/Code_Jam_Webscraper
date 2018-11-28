def omi(x,r,c):
    a='GABRIEL'
    b='RICHARD'
    if (x==1):
        return a
    elif(x==2):
        if ((r*c)%x==0):
            return a
        else:
            return b
    elif(x==3):
        if((r*c)%x==0 and (r>=2 and c>=2) and (r>=3 or c>=3)):
            return a
        else:
            return b
    elif(x==4):
        if((r*c)%x==0 and (r>=3 and c>=3) and (r>=4 or c>=4)):
            return a
        else:
            return b

def win(file):
    f=open(file)
    g=open('output.ou',mode='w')
    b=int(f.readline()[:-1])
    for j in range(b):
        (x,r,c)=f.readline()[:-1].split(' ')
        (x,r,c)=(int(x),int(r),int(c))
        v=omi(x,r,c)
        g.write("Case #"+str(j+1)+": "+v+"\n")
    f.close()
    g.close()

