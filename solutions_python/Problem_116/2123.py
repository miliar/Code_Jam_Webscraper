#print 'Hola Mundo'
#a=3
#print 'A vale: {0}'.format(a)
#a=4
input = open('C:\Users\Luis\Desktop\CODE JAM\A-large.in', 'r')

output = open('C:\Users\Luis\Desktop\CODE JAM\output1big.txt', 'w')

casos=int(input.readline())
convertir={'X':10,'T':50,'O':100,'.':0}
#print int(casos)+2
for i in range(casos):
    matriz=[[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]]
    for j in range(4):
        linea=input.readline()
        for k in range(4):
            matriz[j][k]=convertir[linea[k]]
    input.readline() #leo linea de separacion
    
    #Empiezo algoritmo de procesado de la matriz
    resultado=0
    #filas
    for ii in range(4):
        if sum(matriz[ii])==40 or sum(matriz[ii])==80:
            resultado='X won'
        if sum(matriz[ii])==400 or sum(matriz[ii])==350:
            resultado='O won'
    #columnas
    matriz=zip(*matriz)
    for ii in range(4):
        if sum(matriz[ii])==40 or sum(matriz[ii])==80:
            resultado='X won'
        if sum(matriz[ii])==400 or sum(matriz[ii])==350:
            resultado='O won'
    #diagonales
    diag1=matriz[0][0]+matriz[1][1]+matriz[2][2]+matriz[3][3]
    diag2=matriz[0][3]+matriz[1][2]+matriz[2][1]+matriz[3][0]
    if diag1==40 or diag1==80 or diag2==40 or diag2==80:
        resultado='X won'
    if diag1==400 or diag1==350 or diag2==400 or diag2==350:
        resultado='O won'
        
    #compruebo si ya hay ganador
    if resultado==0:
        #compruebo si hay casillas vacias
        for i3 in range(4):
            if 0 in matriz[i3]:
                resultado='Game has not completed'
        if resultado==0:
            resultado='Draw'
                
    print 'Case #{0}: {1}'.format(i+1,resultado)
    output.write('Case #{0}: {1}\n'.format(i+1,resultado))


            
        



input.close()
output.close()

#line = f.readline()