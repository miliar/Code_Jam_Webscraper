f = open("A-large.in")
salida = open("salida.txt", 'w')
numeros = []
for line in f:
    numeros.append(line)
casos = numeros[0]
for caso in range(int(casos)):
    verguenzas = str(numeros[caso+1]).split(" ")[1].strip()
    amigosnecesarios = 0
    totalacumulado = 0
    for pos in range(len(verguenzas)):
        actual = int(verguenzas[pos])
        if (totalacumulado + amigosnecesarios) < pos:
            amigosnecesarios = amigosnecesarios + (pos - (totalacumulado + amigosnecesarios))
        totalacumulado = totalacumulado + actual
    salida.write("Case #" + str(int(caso)+1) + ": " + str(amigosnecesarios)+'\n')
salida.close()