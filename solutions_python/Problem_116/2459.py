from __future__ import print_function

#MAIN
with open('/home/juanycaro/Descargas/A-large.in') as f_in:
    N = [int(x) for x in f_in.readline().split()][0]
    with open('/home/juanycaro/Descargas/salida_large.txt', 'w') as f_out:
        for t in range(N):
            tabla = []
            for i in range(4):
                line = f_in.readline().strip()
                arreglo = list(line)
                tabla.append(arreglo)
            line = f_in.readline().strip()
            oWon = False
            xWon = False
            incompleto = False
            k = 0
            while (not oWon) and (not xWon) and (k < 10):
                T = 0
                O = 0
                X = 0
                if k < 4:
                    # Reviso filas
                    for  j in range(4):
                        if tabla[k][j] == 'O':
                            O += 1
                        elif tabla[k][j] == 'X':
                            X += 1
                        elif tabla[k][j] == 'T':
                            T = 1
                        elif tabla[k][j] == '.':
                            incompleto = True
                elif k < 8:
                    # Reviso columnas
                    for  j in range(4):
                        if tabla[j][k-4] == 'O':
                            O += 1
                        elif tabla[j][k-4] == 'X':
                            X += 1
                        elif tabla[j][k-4] == 'T':
                            T = 1
                        elif tabla[j][k-4] == '.':
                            incompleto = True
                elif k < 9:
                    # Reviso una diagonal
                    for  j in range(4):
                        if tabla[j][j] == 'O':
                            O += 1
                        elif tabla[j][j] == 'X':
                            X += 1
                        elif tabla[j][j] == 'T':
                            T = 1
                        elif tabla[j][j] == '.':
                            incompleto = True
                else:
                    # Reviso la otra diagonal
                    h = 4
                    for  j in range(4):
                        h -= 1
                        if tabla[j][h] == 'O':
                            O += 1
                        elif tabla[j][h] == 'X':
                            X += 1
                        elif tabla[j][h] == 'T':
                            T = 1
                        elif tabla[j][h] == '.':
                            incompleto = True

                k += 1
                oWon = (O+T == 4)
                xWon = (X+T == 4)

            if oWon:
                resul = 'O won'
            elif xWon:
                resul = 'X won'
            elif incompleto:
                resul = 'Game has not completed'
            else:
                resul = 'Draw'

            cadena_std = "Case #" + str(t+1) + ': '
            print(cadena_std + resul, file=f_out)
