i = 0#Numarul liniei la care ma aflu
f = open("Output.txt", "w")
for e in open("Input.txt", "r"):
    if i % 5 == 0:#Daca sunt pe prima linie, sau liniile goale
        m = []
    else:
        if i % 5 == 1:#Prima linie din matrice
            line = []
            for c in e[:-1]:
                line.append(c)
            m.append(line)
        if i % 5 == 2:#A 2-a linie din matrice
            line = []
            for c in e[:-1]:
                line.append(c)
            m.append(line)
        if i % 5 == 3:#A 3-a linie din matrice
            line = []
            for c in e[:-1]:
                line.append(c)
            m.append(line)
        if i % 5 == 4:#Ultima linie din matrice, aici fac prelucrarile
            line = []
            for c in e[:-1]:
                line.append(c)
            m.append(line)
            #print m
            won = 'Draw'
            for k in range(0,4):
                #Verific linia daca a castigat X
                if m[k][0] == 'X' or m[k][0] == 'T':
                    if m[k][1] == 'X' or m[k][1] == 'T':
                        if m[k][2] == 'X' or m[k][2] == 'T':
                            if m[k][3] == 'X' or m[k][3] == 'T':
                                won = 'X won'
                #Verific linia daca a castigat O
                if m[k][0] == 'O' or m[k][0] == 'T':
                    if m[k][1] == 'O' or m[k][1] == 'T':
                        if m[k][2] == 'O' or m[k][2] == 'T':
                            if m[k][3] == 'O' or m[k][3] == 'T':
                                won = 'O won'
                #Verific coloana daca a castigat X
                if m[0][k] == 'X' or m[0][k] == 'T':
                    if m[1][k] == 'X' or m[1][k] == 'T':
                        if m[2][k] == 'X' or m[2][k] == 'T':
                            if m[3][k] == 'X' or m[3][k] == 'T':
                                won = 'X won'
                #Verific coloana daca a castigat O
                if m[0][k] == 'O' or m[0][k] == 'T':
                    if m[1][k] == 'O' or m[1][k] == 'T':
                        if m[2][k] == 'O' or m[2][k] == 'T':
                            if m[3][k] == 'O' or m[3][k] == 'T':
                                won = 'O won'
            #Verific Diagonala principala daca a castigat X
            if m[0][0] == 'X' or m[0][0] == 'T':
                if m[1][1] == 'X' or m[1][1] == 'T':
                    if m[2][2] == 'X' or m[2][2] == 'T':
                        if m[3][3] == 'X' or m[3][3] == 'T':
                            won = 'X won'
            #Verific Diagonala principala daca a castigat O
            if m[0][0] == 'O' or m[0][0] == 'T':
                if m[1][1] == 'O' or m[1][1] == 'T':
                    if m[2][2] == 'O' or m[2][2] == 'T':
                        if m[3][3] == 'O' or m[3][3] == 'T':
                            won = 'O won'
            #Verific Diagonala secundara daca a castigat X
            if m[0][3] == 'X' or m[0][3] == 'T':
                if m[1][2] == 'X' or m[1][2] == 'T':
                    if m[2][1] == 'X' or m[2][1] == 'T':
                        if m[3][0] == 'X' or m[3][0] == 'T':
                            won = 'X won'
            #Verific Diagonala secundara daca a castigat O
            if m[0][3] == 'O' or m[0][3] == 'T':
                if m[1][2] == 'O' or m[1][2] == 'T':
                    if m[2][1] == 'O' or m[2][1] == 'T':
                        if m[3][0] == 'O' or m[3][0] == 'T':
                            won = 'O won'
            if won == 'Draw':
                for element in m:
                    if '.' in element:
                        won = 'Game has not completed'
            rez = "Case #" + str(i / 5 + 1) + ": " + won + "\n"
            f.write(rez)
    i += 1
f.close()
