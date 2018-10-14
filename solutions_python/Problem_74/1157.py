f=open("A-large.in")
fo=open("saida.out","w")
s=f.readline()
n=int(s)
li=0
for line in f:
    li+=1
    #for i in range(len(line))
    line=line[:-1]
    #print line
    to=0
    tb=0
    tt=0
    pO=1
    pB=1
    elements=line.split(' ')
    nE=int(elements[0])
    for i in range(nE):
        #print i*2+1," ", i*2+2
        a=elements[i*2+1]
        b=int(elements[i*2+2])
        if(a=="O"):
            inc=abs(b-pO)+1            
            to=max(tt+1,to+inc)
            tt=to
            pO=b
        else:
            inc=abs(b-pB)+1
            tb=max(tt+1,tb+inc)
            tt=tb
            pB=b
        #print to," ",tb," ",tt
    fo.write("Case #"+str(li)+": "+str(tt)+"\n")
    #print tt
