'''
Created on 12/04/2013

@author: Javier
'''


n = 0
m = 0

menor = 1
mayor = 100



archivo = "B-large.in"
entrada = file(archivo)


def procesaTablero(tablero, caso):
    valido = True
    
    #todo en columna 0
    for i in range(0, n):
        
        for x in range(0, m):
            config = mayor - tablero[i][x]
            #verifica movimiento a -> derecha
            derechaValida = True
            for j in range(0, m):
                delta = mayor - tablero[i][j]
                
                if delta < config:
                    derechaValida = False
                    break;
            
            
            #for x in range(0, m):
            
            #verifica movimiento abajo
            abajoValida = True
            for j in range(0, n):
                delta = mayor - tablero[j][x]
                
                if delta < config:
                    abajoValida = False
                    break;
            
            if not derechaValida and not abajoValida:
                valido = False
    
    #respuesta
    print "Case #" + str(caso) + ":",
    if valido:
        print "YES"
    else:
        print "NO"

casos = int(entrada.readline())

for i in range(casos):
    
    tablero = {}
    info = entrada.readline().split()
    n = int(info[0])
    m = int(info[1])
    
    for j in range(0, n): #equivale a n
        info = entrada.readline().split()
        
        tablero[j] = []
        
        
        for z in range(0,m): #equivale a m
            tablero[j].append(int(info[z]))
            
    
    #procesa
    procesaTablero(tablero, i + 1)