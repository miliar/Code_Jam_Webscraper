f=open("A-small-attempt3.in")
T=int(f.readline())
g=open("A.out","w")
for case in xrange(1,T+1):

    instring=f.readline().rstrip()
    symbols=[]
    for i in instring:
        if i not in symbols:
            symbols.append(i)
    if len(symbols)==1:
        go=1
        num=0
        for i in instring:
            num+=go
            go*=2
        g.write( "Case #"+str(case)+": "+str(num)+"\n")
    else:
        symbols[0],symbols[1]=symbols[1],symbols[0]
        base=len(symbols)
        place=1
        total=0
        for i in xrange(len(instring)-1,-1,-1):
            total+=place*symbols.index(instring[i])
            place*=base
        g.write("Case #"+str(case)+": "+str(total)+"\n")
g.close()
