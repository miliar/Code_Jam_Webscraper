entrada = open("D-small-attempt8.in")
salida = open("d-out.txt", 'w')
valores = {"x":1,"+":1,"o":2,".":0}
for case in xrange(1, int(entrada.readline())+1):
    salida.write("Case #"+str(case)+": ")
    n, m = map(int, entrada.readline().strip().split())
    modelos = {}
    matriz = [["."]*n for _ in xrange(n)]
    def agregar(i,j,t):
        modelos[(i,j)] = t
        matriz[i][j] = t
    for i in xrange(m):
        tipo, fila, col = entrada.readline().split()
        matriz[int(fila)-1][int(col)-1] = tipo
    if n == 1:
        if matriz[0][0] == "o":
            salida.write("2 0\n")
        else :
            salida.write("2 1\n")
            salida.write("o 1 1\n")
        continue
    if n == 2:
        if "o" not in matriz[0]:
            i = 0
            if "x" in matriz[0]:
                i = matriz[0].index("x")
            agregar(0,i,"o")
        for i in xrange(2):
            if matriz[0][i] == ".":
                agregar(0,i,"+")
        i = matriz[0].index("o")
        agregar(1-i,1-i,"x")
        salida.write(str(sum(valores[matriz[i][j]] for i in xrange(n) for j in xrange(n)))+" "+str(len(modelos.keys()))+"\n")
        for i in modelos:
            salida.write(modelos[i]+" "+str(i[0]+1)+" "+str(i[1]+1)+"\n")
        continue
    for i in xrange(1,n-2):
        agregar(n-1,i,"+")
    if "x" in matriz[0]:
        agregar(0,matriz[0].index("x"),"o")
    elif "o" not in matriz[0]:
        agregar(0,0,"o")
    indice = matriz[0].index("o")
    if indice != 0:
        agregar(indice,0,"x")
    else :
        agregar(n-2,n-1,"x")
    if indice != n-2 and indice != n-1:
        agregar(n-1,n-2,"o")
    elif indice != n-1 :
        agregar(n-1,n-2,"+")
        agregar(n-1,n-1,"x")
    else :
        agregar(n-1,n-2,"+")
        agregar(n-2,n-2,"x")
    if "x" not in matriz[n-2]:
        agregar(n-2,n-1,"x")
    for i in xrange(1,n-2):
        if i != indice:
            agregar(i,i,"x")
    for i in xrange(n):
        if matriz[0][i] == ".":
            agregar(0,i,"+")
    salida.write(str(sum(valores[matriz[i][j]] for i in xrange(n) for j in xrange(n)))+" "+str(len(modelos.keys()))+"\n")
    for i in modelos:
        salida.write(modelos[i]+" "+str(i[0]+1)+" "+str(i[1]+1)+"\n")