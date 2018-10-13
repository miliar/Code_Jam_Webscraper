
inp=open('a.in','r')
T=int(inp.readline())

out=open('a.out','w')

def nextinst(indice,quien,cual):
    inst=dict()
    olisto=False
    blisto=False
    for i in range(indice,len(quien)):
        if quien[i]=='O' and not olisto:
            inst['O']=cual[i]
            olisto=True
        elif quien[i]=='B' and not blisto:
            inst['B']=cual[i]
            blisto=True
        if olisto and blisto:
            break
    return inst
             
def distancias(pos,inst):
    dist=dict()
    if 'O' in inst: dist['O']=abs(pos['O']-inst['O'])
    if 'B' in inst: dist['B']=abs(pos['B']-inst['B'])
    return dist


for caso in range(T):
    tiempo=0
    linea=inp.readline().strip().split(' ')
    quien=linea[1::2]
    cual=linea[2::2]
    for i in range(len(cual)):
        cual[i]=int(cual[i])
    assert len(quien)==len(cual)
    pos={'O':1,'B':1}

    
    for indice in range(len(quien)):
        #al que no le toca se mueve hasta su boton y espera
        #al que le toca
        inst=nextinst(indice,quien,cual)
        bot=quien[indice]
        otro='B' if bot=='O' else 'O'
        dist=distancias(pos,inst)
        pos[bot]=cual[indice]
        tiempo+=dist[bot]+1

        if otro in inst:
            if dist[otro]<=dist[bot]+1:
                pos[otro]=inst[otro]
            else:
                pos[otro]=pos[otro]+(dist[bot]+1)*(1 if inst[otro]>pos[otro] else -1)

    print tiempo
    out.write('Case #'+str(caso+1)+': '+str(tiempo)+'\n')
out.close()
    
