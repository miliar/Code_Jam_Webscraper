with open('A-large.in') as file:
    ain=file.readlines()
cases=int(ain[0])
line=1
wfile=open('out.txt','w')
for case in range(cases):
    RC=ain[line].split()
    line+=1
    R=int(RC[0])
    C=int(RC[1])
    cake=[]
    init=[]
    for i in range(R):
        tline=ain[line].rstrip()
        cake.append(list(tline))
        line+=1
        j=0
        for char in tline:
            if(not char=='?'):
                init.append([char,i,j])
            j+=1
    for sym in init:
        jleft=sym[2]-1
        jright=sym[2]+1
        iup=sym[1]-1
        idown=sym[1]+1
        if(jright<C):
            while(cake[iup+1][jright]=='?'):
                jright+=1
                if(jright==C):
                    break
        jright-=1
        if(jleft>=0):
            while(cake[iup+1][jleft]=='?'):
                jleft-=1
                if(jleft<0):
                    break
        jleft+=1
        checkup=True
        if(iup>=0):
            while checkup:
                for j in range(jleft,jright+1):
                    if(not cake[iup][j]=='?'):
                        checkup=False
                        break
                if(not checkup):
                    break
                iup-=1
                if(iup<0):
                    break
        iup+=1
        checkdown=True
        if(idown<R):
            while checkdown:
                for j in range(jleft,jright+1):
                    if(not cake[idown][j]=='?'):
                        checkdown=False
                        break
                if(not checkdown):
                    break
                idown+=1
                if(idown==R):
                    break
        idown-=1
        for q in range(iup,idown+1):
            for r in range(jleft,jright+1):
                cake[q][r]=sym[0]
    wfile.write("Case #{}:\n".format(case+1))
    for x in range(R):
        wfile.write("{}\n".format("".join(cake[x])))
wfile.close()
