#!/usr/bin/python

caso_completo = []
trovato = 0
win = ''
cntcasi = 1

with open('small2.in') as f:
    i = 0
    casi = f.read(1)

    for x in f.readlines():

        if(i == 0):
            casi = x
            #print casi
        elif x == '\n':
            # E' finito il caso
            #print caso_completo

            # Cerco per colonne
            if trovato == 0:

                col = ''
                c = 0
                while (c < 4):
                    r = 0
                    #print c
                    while ( r < 4):
                        col = col + caso_completo[r][c]
                        r +=1


                    if col.count('X') >= 3:
                        if col.count('T') >= 1 or col.count('X') == 4:
                            #print 'X ha vinto'
                            win = 'X'
                            trovato = 1
                    elif col.count('O') >= 3:
                        if col.count('T') >= 1 or col.count('O') == 4:
                            #print 'O ha vinto'
                            win = 'O'
                            trovato = 1
                    col = ''
                    c += 1
            #cerco per diagonali
            if (trovato == 0):
                diag1 = ''
                diag2 = ''
                d = 0
                d2 = 3
                while (d < 4):
                    diag1 = diag1 + caso_completo[d][d]
                    diag2 = diag2 +caso_completo[d][d2]
                    d += 1
                    d2 -= 1

                if diag1.count('X') >= 3:
                    if diag1.count('T') >= 1 or diag1.count('X') == 4:
                        #print 'X ha vinto'
                        win = 'X'
                        trovato = 1
                if diag2.count('X') >= 3:

                    if diag2.count('T') >= 1 or diag2.count('X') == 4:
                        #print 'X ha vinto'
                        win = 'X1'
                        trovato = 1

                if diag1.count('O') >= 3:
                    if diag1.count('T') >= 1 or diag1.count('O') == 4:
                        #print 'O ha vinto'
                        trovato = 1
                        win = 'O'
                if diag2.count('O') >= 3:
                    if diag2.count('T') >= 1 or diag2.count('O') == 4:
                        #print 'O ha vinto'
                        win = 'O'
                        trovato = 1


            if trovato == 1:
                print "Case #%d: %s won" % (cntcasi,win)

            else:
            #controllo pareggio
                c = 0
                for par in caso_completo:
                    if par.count('.') > 0:
                        c +=1

                if c == 0:
                    print "Case #%d: Draw" % cntcasi
                    trovato = 1
                elif c > 0:
                    print "Case #%d: Game has not completed" % cntcasi
                    trovato = 1

            caso_completo = []
            trovato = 0
            cntcasi += 1
        else:

            riga = x[0:4]
            #print riga
            if riga.count('X') >= 3:
                # X ha vinto!!
                #break
                if riga.count('T') >= 1 or riga.count('X') == 4:
                    #print 'X ha vinto'

                    win = 'X'
                    trovato = 1

            elif riga.count('O') >= 3:
                # O ha vinto!!
                #break
                if riga.count('T') >= 1 or riga.count('0') == 4:
                    #print 'O ha vinto'
                    win = 'O'
                    trovato = 1

            caso_completo.append(riga)
        i += 1


i = 0