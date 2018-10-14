f=open("b.in")
g=open("b.out","w")
i=0
for line in f.readlines()[1:]:
    i+=1
    g.write("Case #"+str(i)+": ")
    line=map(int,line.split())
    s=line[1]
    p=line[2]
    nr=0
    for x in line[3:]:
        if x >= p:
            if x >= 3*p-2:
                nr+=1
            elif x >= 3*p-4 and s > 0:
                nr+=1
                s-=1
    g.write(str(nr)+"\n")
g.close()
