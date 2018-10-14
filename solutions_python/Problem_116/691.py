'''
Created on 13/04/2013

@author: Carles
'''

inFile = open('input.in', 'r')
outFile = open('output.out', 'w')

numCasos = inFile.readline()

for i in range(int(numCasos)):
    tablero=[None]*4
    for j in range(4):
        linea=inFile.readline()
        tablero[j] = linea[:4]
    inFile.readline()
    
    #print "#"+str(i)+" "+str(tablero)
    
    #columnas
    for j in range(4):
        ganador = True
        if tablero[0][j] == '.':
            ganador = False
            continue
        if tablero[0][j] != 'T':
            jug = tablero[0][j]
        else:
            if tablero[1][j] == '.':
                ganador = False
                continue
            else:
                jug = tablero[1][j]
        for k in range(4):
            if(tablero[k][j] != jug and tablero[k][j] != 'T'):
                ganador = False
                break
        if ganador:
            break
        
    if ganador:
        outFile.write("Case #"+str(i+1)+": "+jug+" won")
        print "Case #"+str(i+1)+": "+jug+" won"
    else: 
        #print "empate o sigue jugando"
        #filas
        for j in range(4):
            ganador = True
            if tablero[j][0] == '.':
                ganador = False
                continue
            if tablero[j][0] != 'T':
                jug = tablero[j][0]
            else:
                if tablero[j][1] == '.':
                    ganador = False
                    continue
                else:
                    jug = tablero[j][1]
            for k in range(4):
                if(tablero[j][k] != jug and tablero[j][k] != 'T'):
                    ganador = False
                    break
            if ganador:
                break
            
        if ganador:
            outFile.write("Case #"+str(i+1)+": "+jug+" won")
            print "Case #"+str(i+1)+": "+jug+" won"
        else:
            #diagonales
            ganador = True
            for j in range(4):
                if tablero[j][j] == '.':
                    ganador = False
                    continue
                if tablero[0][0] != 'T':
                    jug = tablero[0][0]
                else:
                    if tablero[1][1] == '.':
                        ganador= False
                        continue
                    else:
                        jug = tablero[1][1]
                if(tablero[j][j] != jug and tablero[j][j] != 'T'):
                    ganador = False
                    break
            
            if ganador:
                outFile.write("Case #"+str(i+1)+": "+jug+" won")
                print "Case #"+str(i+1)+": "+jug+" won"
            else:
                ganador = True
                for j in range(4):
                    if tablero[j][3-j] == '.':
                        ganador = False
                        continue
                    if tablero[0][3] != 'T':
                        jug = tablero[0][3]
                    else:
                        if tablero[1][2] == '.':
                            ganador = False
                            continue
                        else:
                            jug = tablero[1][2]
                    if(tablero[j][3-j] != jug and tablero[j][3-j] != 'T'):
                        ganador = False
                        break
            
                if ganador:
                    outFile.write("Case #"+str(i+1)+": "+jug+" won")
                    print "Case #"+str(i+1)+": "+jug+" won"
                else:
                    sigueJugando = False
                    for j in range(4):
                        for k in range(4):
                            if tablero[j][k]=='.':
                                sigueJugando = True
                                break
                    if sigueJugando:
                        outFile.write("Case #"+str(i+1)+": Game has not completed")
                        print "Case #"+str(i+1)+": Game has not completed"
                    else:
                        outFile.write("Case #"+str(i+1)+": Draw")
                        print "Case #"+str(i+1)+": Draw"
            
    outFile.write("\n")
inFile.close()
outFile.close()