goin=open("B.in","r")
t=int(goin.readline().strip())
outs=list()


for i in range(t):
    xd=list(map(int, goin.readline().strip().split()))
    ac=xd[0]
    aj=xd[1]
    clist=list()
    jlist=list()
    for j in range(ac):
        lol=list(map(int, goin.readline().strip().split()))
        lol.append("c")
        clist.append(lol)
    for j in range(aj):
        lol=list(map(int, goin.readline().strip().split()))
        lol.append("j")
        jlist.append(lol)
    alist=clist+jlist
    alist=sorted(alist, key = lambda x: x[0])
    print(alist)
    vahedc=list() #millest saab c votta
    vahedj=list()
    muutused=0
    pc=0
    pcmax=0
    pj=0
    pjmax=0
    for j in range(1,len(alist)):
        if alist[j][2]=="c" and alist[j-1][2]=="c":
            pc+=alist[j][0]-alist[j-1][0]
            pcmax+=alist[j][0]-alist[j-1][0]
            vahe=alist[j][0]-alist[j-1][1]
            vahedj.append(vahe)
        if alist[j][2]=="j" and alist[j-1][2]=="j": 
            pj+=alist[j][0]-alist[j-1][0]
            pjmax+=alist[j][0]-alist[j-1][0]
            vahe=alist[j][0]-alist[j-1][1]
            vahedc.append(vahe)
        if alist[j][2]=="j" and alist[j-1][2]=="c":
            pc+=alist[j-1][1]-alist[j-1][0]
            pcmax+=alist[j][0]-alist[j-1][0]
            pjmax+=alist[j][0]-alist[j-1][1]
            muutused+=1
        if alist[j][2]=="c" and alist[j-1][2]=="j":
            pj+=alist[j-1][1]-alist[j-1][0]
            pjmax+=alist[j][0]-alist[j-1][0]
            pcmax+=alist[j][0]-alist[j-1][1]
            muutused+=1
    print(muutused)
    if alist[0][2]=="c" and alist[-1][2]=="c":
        pc+=alist[0][0]+(1440-alist[-1][0])
        vahe=alist[0][0]+(1440-alist[-1][1])
        vahedj.append(vahe)
    if alist[0][2]=="j" and alist[-1][2]=="j":
        pj+=alist[0][0]+1440-alist[-1][0]
        vahe=alist[0][0]+1440-alist[-1][1]
        vahedc.append(vahe)
    if alist[0][2]=="j" and alist[-1][2]=="c":
        pc+=alist[0][1]+1440-alist[-1][0]
        muutused+=1
    if alist[0][2]=="c" and alist[-1][2]=="j":
        pj+=alist[0][1]+1440-alist[-1][0]
        muutused+=1
    print(muutused)
    vahedc=sorted(vahedc, reverse=True)
    vahedj=sorted(vahedj, reverse=True)
    for asi in vahedc:
        if pc<=720:
            break
        pc-=asi
        pjmax+=asi
        muutused+=2
    for asi in vahedj:
        if pj<=720:
            break
        pj-=asi
        pcmax+=asi
        muutused+=2
    for asi in vahedc:
        if pcmax>=720:
            break
        pcmax+=asi
        muutused+=2
    for asi in vahedj:
        if pjmax>=720:
            break
        pjmax+=asi
        muutused+=2
    outt="Case #"+str(i+1)+": "+str(muutused)+"\n"
    outs.append(outt)
goin.close()



goout=open("B.out","w")
for i in range(t):
    goout.write(outs[i])
goout.close()
