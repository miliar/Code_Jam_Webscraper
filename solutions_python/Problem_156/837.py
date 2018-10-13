f = open("B-small-attempt3.in")
salida = open("salida.txt", 'w')
casos = int(f.readline())
def resolverDistribucion(distribucionActual, minutosSumados, minutosMinimos):
    if minutosSumados >= minutosMinimos:
        return minutosMinimos
    nuevaDistribucion = distribucionActual[:]
    maximo = max(nuevaDistribucion)
    nuevaDistribucion.remove(maximo)
    nuevaDistribucion.append(maximo/2)
    nuevaDistribucion.append(maximo - (maximo/2))
    if (float(maximo)**0.5 != int(float(maximo)**0.5)) or (maximo == 1):
        return int(min(minutosMinimos, resolverDistribucion(nuevaDistribucion, minutosSumados+1, min(minutosMinimos, maximo+minutosSumados)), maximo+minutosSumados ))
    else :
        segundaDistribucion = distribucionActual[:]
        segundaDistribucion.remove(maximo)
        for i in range(int(maximo**0.5)):
            segundaDistribucion.append(maximo**0.5)
        return int(min(minutosMinimos, resolverDistribucion(nuevaDistribucion, minutosSumados+1, min(minutosMinimos, maximo+minutosSumados)), resolverDistribucion(segundaDistribucion, minutosSumados+maximo**0.5-1, min(maximo+minutosSumados, minutosMinimos)), maximo+minutosSumados ))


for caso in range(casos):
    platos = int(f.readline())
    distribucion = str(f.readline())
    distribuciones = distribucion.split(" ")
    intDistribuciones = []
    for i in distribuciones:
        intDistribuciones.append(int(i))
    intDistribuciones.sort(reverse = True)
#    print intDistribuciones
#    print "Case #" + str(int(caso)+1) + ": " + str(resolverDistribucion(intDistribuciones, 0, intDistribuciones[0]))+'\n'
    salida.write("Case #" + str(int(caso)+1) + ": " + str(resolverDistribucion(intDistribuciones, 0, intDistribuciones[0]))+'\n')
salida.close()
