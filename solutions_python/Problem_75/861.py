def insertar(lista, elemento, coms, opps):
    if(len(lista) == 0):
        lista.append(elemento)
    else:
        end = lista[len(lista)-1]
        if((end + elemento) in coms ):
            lista[len(lista)-1] = coms[end + elemento]
        elif((elemento + end) in coms):
            lista[len(lista)-1] = coms[elemento + end]
        else:
            for i in lista:
                a = i + elemento
                b = elemento + i
                if(a in opps or b in opps):
                    lista = []
                    return lista
            lista.append(elemento)
    return lista

def leerLinea(linea):
    datos = linea.split()
    posi = 0
    C = int( datos[posi])
    coms =  {}
    posi = posi + 1
    for i in range(C):        
        combinacion = datos[posi]
        posi = posi + 1
        coms[combinacion[0:2]] = combinacion[2]
        coms[(combinacion[0:2])[::-1]] = combinacion[2]

    D = int(datos[posi])
    posi = posi + 1
    opps = set()
    for i in range(D):
        opuesto = datos[posi]
        posi = posi + 1
        opps.add(opuesto)
        opps.add(opuesto[::-1])
    cadena = ""
    if (posi < len(datos)):
        N = int(datos[posi])
        posi = posi + 1
        cadena = datos[posi]
    return cadena, coms, opps
        
def invoke(linea):
    cadena, coms, opps = leerLinea(linea)
    lista = []
    for i in cadena:
        lista = insertar(lista, i, coms, opps)
    return lista
    
def solver(name):
    arch = file(name, "r")
    output = file(name + ".out", "w")
    outstr = ""
    N = int(arch.readline())
    lines  =arch.readlines()
    for i in range(N):
        line = lines[i]
        outstr = outstr + "Case #" + str(i + 1) + ": "
        lista = invoke(line)
        if(len(lista) == 0):
            outstr = outstr + "[]\n"
        else:
            outstr = outstr + "["
            for i in lista:
                outstr = outstr + i + ", "
            outstr = outstr[0:len(outstr)-2]
            outstr = outstr + "]\n"

    output.write(outstr)
    output.close()
    arch.close()
