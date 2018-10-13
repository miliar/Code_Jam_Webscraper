fi=open("A-large.in",'r')
fo=open("A-large.out",'w')

t=int(fi.readline())
for i in range(t):
    s=fi.readline().split()
    n=int(s[0])
    j=1
    ins=[]
    while j<(2*n): 
        ins.append((s[j],int(s[j+1])))
        j=j+2
    to=0
    tb=0
    poso=1
    posb=1
    if (ins[0][0]=='O'):
        poso=ins[0][1]
        to=poso
    else:
        posb=ins[0][1]
        tb=posb
    for j in range(1,n):
        if ins[j][0]==ins[j-1][0]:
            if ins[j][0]=='O':
                to+=abs(ins[j][1]-ins[j-1][1])+1
                poso=ins[j][1]
            else:
                tb+=abs(ins[j][1]-ins[j-1][1])+1
                posb=ins[j][1]
        else:
            if ins[j][0]=='O':
                to+=abs(ins[j][1]-poso)
                to=max(tb,to)+1
                poso=ins[j][1]
            else:
                tb+=abs(ins[j][1]-posb)
                tb=max(tb,to)+1
                posb=ins[j][1]
                
    fo.write("Case #"+str(i+1)+": "+str(max(to,tb))+"\n")
             
fi.close()
fo.close()