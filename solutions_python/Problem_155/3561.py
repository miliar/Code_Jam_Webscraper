archivo=open('resultado.txt','w')
#---------------------------------------------------------
NumerosdeCasos = int(input("Numero de casos: "))
for k in range(NumerosdeCasos):
    NumeroPersonas = 0
    amigos = 0
    cadenatimidez = str(input("Cadena de personas timidez: " ))
    Maximatimidez = int(cadenatimidez[0])
    for j in range(Maximatimidez+1):
        if NumeroPersonas>=j:
            NumeroPersonas = NumeroPersonas + int(cadenatimidez[j+2])
        else:
            faltantes = j -NumeroPersonas
            NumeroPersonas = NumeroPersonas + faltantes
            NumeroPersonas = NumeroPersonas + int(cadenatimidez[j+2])
            amigos = amigos + faltantes
    x= int(k) + 1
    arhivo = archivo.write('Case #'+str(x)+': '+str(amigos)+'\n')
archivo.close()
