def numeroCambios(buscadores, consultas, idxNoUsar):
    total=0
    proxNoUsar=-1
    while len(consultas)>0:
        i=0
        maxPosAparicion=0
        buscadorAparicion=-1

        while i<len(buscadores):
            if i!=idxNoUsar:
                try:
                    posAparicion=consultas.index(buscadores[i])
                except ValueError:
                    return total

                if posAparicion>maxPosAparicion:
                    maxPosAparicion=posAparicion
                    proxNoUsar=i
            
            i+=1

        total+=1
        consultas=consultas[maxPosAparicion:]

    return total
        
#    return 1+numeroCambios(buscadores,consultas[maxPosAparicion:],proxNoUsar)


def leerCaso(fr):
    numBuscadores=int(fr.readline())
    i=0
    buscadores=[]
    while i<numBuscadores:
        buscadores.append(fr.readline().split('\n'))
        i+=1

    numConsultas=int(fr.readline())
    i=0
    consultas=[]
    while i<numConsultas:
        consultas.append(fr.readline().split('\n'))
        i+=1

    return numeroCambios(buscadores,consultas,-1)



fr=open('A-large.in','r')
fw=open('A-large.out','w')

numCasos=int(fr.readline())

i=1
while i<=numCasos:
    out=leerCaso(fr)
    fw.write("Case #%d: %d\n" %(i,out))

    i+=1

fr.close()
fw.close()
