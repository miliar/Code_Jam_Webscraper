import sys
import re

if len(sys.argv) != 3:
    print 'Usage: ' + sys.argv[0] + ' input output'
    exit()
SEntrada = sys.argv[1]
SSalida = sys.argv[2]

entrada = open(SEntrada,'r')
salida = open(SSalida,'w')
configuracion = entrada.readline()
configuracion = configuracion.split()
Longitud = int(configuracion[0])
Palabras = int(configuracion[1])
Casos = int(configuracion[2])

LPalabra = []
for palabra in range(Palabras):
    LPalabra.append(entrada.readline())

for caso in range(Casos):
    re.purge()
    expresion = entrada.readline()
    expresion = expresion.replace('(','[')
    expresion = expresion.replace(')',']')
      
    contador = 0
    for palabra in LPalabra:
        m = re.search(expresion[:len(expresion)-1],palabra[:len(palabra)-1])
        if m:
            contador += 1
    salida.write('Case #'+str(caso+1)+': '+str(contador)+'\n')

entrada.close()
salida.close()
