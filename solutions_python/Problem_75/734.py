inp=file('b.in','r')
T=int(inp.readline())
out=file('b.out','w')

for caso in range(T):
    linea=inp.readline().strip().split(' ')
    comb=dict()
    op=list()
    C=int(linea[0])
    for i in linea[1:C+1]:
        comb[i[:2]]=i[2]
    D=int(linea[C+1])
    for i in linea[C+2:C+2+D]:
        op.append(i)

    entrada=linea[-1]
    pila=""
    for i in entrada:
        pila+=i
        if pila[-2:] in comb:
            letra=comb[pila[-2:]]
            pila=pila[:-2]+letra
        elif pila[:-3:-1] in comb:
            letra=comb[pila[:-3:-1]]
            pila=pila[:-2]+letra
        for x in pila[:-1]:
            if len(pila)>=2 and (x+pila[-1] in op or pila[-1]+x in op):
                pila=""

    print caso
    out.write("Case #"+str(caso+1)+": "+str(list(pila)).replace("'","")+"\n")
    

out.close()
