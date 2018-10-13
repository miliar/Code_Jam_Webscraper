'''
Created on 13/04/2012

@author: harold
'''

archivo = open('B-large.bin')
lista = archivo.readlines()
limite = lista.pop(0)

def calificar(linea):
    if len(linea) - 1 == '\n':
        linea = linea[0:-1].split(' ')
    else:
        linea = linea.split(' ')
    respuesta = 0
    especiales = int(linea[1])
    minimo = int(linea[2])
    googlers = linea[3:]
    for g in googlers:
        j1 = minimo
        if especiales:
            j2 = j1 - 2
            if j2 < 0:
                j2 = 0
        else:
            j2 = j1 - 1
            if j2 < 0:
                j2 = 0
        j3 = j2
        if int(g) >= j1 + j2 + j3:
            while(not j1 == j2 == j3):
                if j1 + j2 + j3 > int(g):
                    break
                elif j1 + j2 + j3 == int(g):
                    if j1 - j2 == 2 or j1 - j3 == 2:
                        if especiales:
                            especiales -= 1
                            j1 = j2 = j3
                        else:
                            break
                    else:
                        j1 = j2 = j3
                else:
                    if j2 > j3:
                        j3 += 1
                    else:
                        j2 += 1
            else:
                respuesta += 1
    return str(respuesta)
        

respuesta = [calificar(x) for x in lista]
out = open('archivo.out', 'w')
contador = 1
for linea in respuesta[0:int(limite)]:
    out.write('Case #%i: %s\n' % (contador, linea))
    contador += 1

print 'Terminado'
