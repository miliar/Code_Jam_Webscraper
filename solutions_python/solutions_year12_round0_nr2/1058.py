fil=open('input.txt','r')
a=int(fil.readline())
na=a
an=[]
while a>0:
    an1=0
    b=fil.readline()
    b=b.split()
    k=0
    for i in b:
        b[k]=int(i)
        k=k+1
    sm1=(b[2]*3)-4
    sm2=(b[2]*3)-3
    k=3
    #print(sm1,sm2)
    while k<(3+b[0]):
        #print(b[k])
        if b[k]>sm2:
            an1=an1+1
        elif (b[k]==sm1 and b[1]>0 and b[k]>0):
            b[1]=b[1]-1
            an1=an1+1
        elif (b[k]==sm2 and b[1]>0 and b[k]>0):
            an1=an1+1
            b[1]=b[1]-1
        k=k+1
    an.append(str(an1))
    a=a-1
pp=0
bf=open('output.txt','w')
while pp<na:
    per=str(pp+1)
    per='Case #'+per+': '+an[pp]
    bf.write(per+'\n')
    pp=pp+1
fil.close()
bf.close()
