'''
Created on 12/04/2013

@author: Javier
'''

archivo = "A-large.in"
entrada = file(archivo)


jugador_x = "X"
jugador_0 = "O"
comodin = "T"
libre = "."


def procesaTablero(tablero, caso):
    
    libres = 0
    celda = ""
    for i in range(0, 4):
        
        #vertical
        celda = tablero[0][i]
        encontre = 1
        for j in range(1,4):
            tmp = tablero[j][i]
            if tmp != libre:
                if j == 1 and celda == comodin:
                    celda = tmp
                    
                if celda == tmp or tmp == comodin:
                    encontre = encontre + 1
            else:
                libres = libres + 1
                break
        
        if encontre == 4 and celda != libre:
            break
        
        #busqueda horizontal
        celda = tablero[i][0]
        encontre = 1
        for j in range(1,4):
            tmp = tablero[i][j]
            if tmp != libre:
                if j == 1 and celda == comodin:
                    celda = tmp
                    
                if celda == tmp or tmp == comodin:
                    encontre = encontre + 1
            else:
                libres = libres + 1
                break
                
        if encontre == 4 and celda != libre:
            break
        
        #busqueda diagonal izquierda abajo
        if i == 0:
            celda = tablero[0][0]
            encontre = 1
            for j in range(1,4):
                tmp = tablero[j][j]
                if tmp != libre:
                    if j == 1 and celda == comodin:
                        celda = tmp
                        
                    if celda == tmp or tmp == comodin:
                        encontre = encontre + 1
                else:
                    libres = libres + 1
                    break
                
            if encontre == 4 and celda != libre:
                break
            
        #busqueda diagonal derecha abajo 
        if i == 0:
            celda = tablero[0][3]
            encontre = 1
            for j in range(1,4):
                tmp = tablero[j][3 - j]
                if tmp != libre:
                    if j == 1 and celda == comodin:
                        celda = tmp
                        
                    if celda == tmp or tmp == comodin:
                        encontre = encontre + 1
                else:
                    libres = libres + 1
                    break
                
            if encontre == 4 and celda != libre:
                break
    
    #analiza respuesta
    print "Case #" + str(caso) + ": ",
    
    if encontre == 4:
        if celda == jugador_x:
            print "X won"
        else:
            print "O won"
    elif libres == 0:
        print "Draw"
    else:
        print "Game has not completed"
            
            
            
            







casos = int(entrada.readline())

for i in range(casos):
    
    tablero = {}
    for j in range(0, 4):
        linea = entrada.readline()

        tablero[j] = {}
        
        
        for z in range(0,4):
            tablero[j][z] = linea[z : z +1]
            
    entrada.readline()
    
    #procesa tablero
    procesaTablero(tablero, i + 1)