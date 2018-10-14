import sys

cofres=[]
llaves=[0]*201
faltan=0
memoria={}
N=0

malo=' IMPOSSIBLE'

def abre(i):
    global llaves,cofres
    # usar la llave
    llaves[cofres[i][0]]-=1
    # agregar las llaves que hay en el
    for llave in cofres[i][2:]:
        llaves[llave]+=1

def cierra(i):
    global llaves,cofres
    # agregar la llave que lo abrio
    llaves[cofres[i][0]]+=1
    # guardar las llaves que hay en el
    for llave in cofres[i][2:]:
        llaves[llave]-=1    

def busca():
    global cofres,llaves,faltan,memoria,N
    if faltan==0:
        return ''
    if faltan in memoria:
        return memoria[faltan]
    for i in range(0,N):
        if (faltan&(1<<i))==0:
            continue
        if llaves[cofres[i][0]]==0:
            # no puede abrirse, brincarlo
            continue
        # abrirlo
        abre(i)
        faltan^=1<<i
        resultado=busca()
        # cerrarlo
        cierra(i)
        faltan^=1<<i
        if resultado!=malo:
            memoria[faltan]=" {0}{1}".format(i+1,resultado)
            return memoria[faltan]
    memoria[faltan]=malo
    return malo

def Treasure(fname,sname):
    global cofres,llaves,faltan,N,memoria
    with open(fname) as file:
        with open(sname,'w') as salida:
            line = file.readline()
            T=int(line)
            for case in range(1,T+1):
                [K,N]=[int(i) for i in file.readline().split()]
                cofres=[]
                llaves=[0]*201
                faltan=(1<<N)-1
                memoria={}
                for ii in file.readline().split():
                    i=int(ii)
                    llaves[i]+=1
                for n in range(0,N):
                    cofres.append([int(i) for i in file.readline().split()])
                salida.write("Case #{0}:{1}\n".format(case,busca()))
                print("Listo {0}".format(case))
        salida.close()
    file.close()
