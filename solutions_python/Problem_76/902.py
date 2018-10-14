'''
Created on 07/05/2011

@author: Shinjidev
'''

def obtenerSumaListaBinary(lista):
    suma = "000000000000000000000000"
    for i in lista:
        suma = sumaStr(suma, i)
    return suma

def obtenerSumaDecimal(lista):
    suma = 0
    for i in lista:
        suma+=i
    return suma
    

def obtenerListadif(original, l):
    a = []
    for i in original:
        a.append(i)
    for x in l:
        if a.count(x) > 0:
            a.remove(x)
    return a

def generaListaCombinatoria(l, n):
    a = combinations(l,n)
    output = []
    for i in a:
        output.append(i)
    return output

def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = range(r)
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

def Denary2Binary(n):
    '''convert denary integer n to binary string bStr'''
    bStr = ''
    if n < 0:  raise ValueError, "must be a positive integer"
    if n == 0: return '0'
    while n > 0:
        bStr = str(n % 2) + bStr
        n = n >> 1
    return bStr

def binaryToDecimal(n):
    return int(n,2)

def sumaStr(num1, num2):
    i = 0
    output = ""
    while i < 24:
        if num1[i] != num2[i]:
            output += "1"
        else:
            output += "0"
        i+=1
    return output


f = open("C-small-attempt1.in")
fileOutput = open("outputCandy2.txt", "w")
nLinea = 0
cont = 0
caso = 1
for line in f:
    if (nLinea > 0):
        if cont > 0:
            print line
            cont = 0
            mayorTotal = -1
            ##lets start
            ##contiene los ints posibles
            lista = []
            indice = line.find(" ")
            while indice != -1:
                lista.append(int(line[:indice]))
                line = line[indice + 1:]
                indice = line.find(" ")
            lista.append(int(line))
            #ya termine de tener los enteros
            cant = 1
            while cant < len(lista):
                lista1 = generaListaCombinatoria(lista, cant)
                for iteracion in lista1:
                    lista2 = obtenerListadif(lista, iteracion)
                    listaBinary1 = []
                    for i in iteracion:
                        listaBinary1.append(Denary2Binary(i).zfill(24))
                    listaBinary2 = []
                    for i in lista2:
                        listaBinary2.append(Denary2Binary(i).zfill(24))
                    sumaBinary1 = obtenerSumaListaBinary(listaBinary1)
                    sumaBinary2 = obtenerSumaListaBinary(listaBinary2)
                    ##en este caso procedemos a ver cual es mayor
                    if sumaBinary1 == sumaBinary2:
                        suma1 = obtenerSumaDecimal(iteracion)
                        suma2 = obtenerSumaDecimal(lista2)
                        mayor = 0
                        if suma1> suma2:
                            mayor = suma1
                        else:
                            mayor = suma2
                        if mayor > mayorTotal:
                            mayorTotal = mayor     
                cant +=1
            strOutput = "Case #" + str(caso) + ": "
            if mayorTotal == -1:
                strOutput += "NO"
            else:
                strOutput += str(mayorTotal)
            strOutput += "\n"
            fileOutput.write(strOutput)
            caso +=1
        else:
            cont+=1
    nLinea +=1
f.close()
fileOutput.close()