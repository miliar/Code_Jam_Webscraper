import numpy as np
import random as rx
import math
import os



f = open('input.txt', 'r')
numcases = int(f.readline().rstrip('\n'))

for cc in range(1,numcases+1):
    x = f.readline().rstrip('\n')
    xb = x.split()

    Hme = int(xb[0])
    Ame = int(xb[1])
    Hk  = int(xb[2])
    Ak  = int(xb[3])
    B   = int(xb[4])
    D   = int(xb[5])

    sol = 50000

    if (D == 0):
        irange = 0
    else:
        irange = min(100,math.ceil(Ak/D+1))
    irange = int(irange)
    if (B==0):
        jrange = 0
    else:
        jrange = min(100,math.ceil((Hk-Ame)/B+1))

    jrange = int(jrange)
    for i in range(irange+1):
        for j in range(jrange+1):

            Hme2 = Hme
            Ame2 = Ame
            Hk2 = Hk
            Ak2 = Ak
            moves = 0
            for k in range(i):
                if (Ak2-D >= Hme):
                    moves = 50000
                    break
                #elif (Ak2+Ak2-D>=Hme ):
                #    moves = 50000
                #    break
                elif (Ak2-D >= Hme2 ):
                    Hme2 = Hme #reset health
                    Hme2 = Hme2 - Ak2 #take damage
                    Ak2 = max(Ak2-D,0)  #debuff
                    Hme2 = Hme2 - Ak2 #take damage
                    if (Hme2 <= 0):
                        moves = 50000
                        break
                    moves = moves + 2
                else:
                    Ak2 = Ak2-D
                    Hme2 = Hme2 - Ak2 #take damage
                    moves = moves + 1
            if moves < 50000:
                for l in range(j):
                    if (Ak2 >= Hme):
                        moves = 50000
                        break
                    #elif (Ak2+Ak2>=Hme and Ame2+B < Hk2):
                    #    moves = 50000
                    #    break
                    elif (Ak2 >= Hme2):
                        Hme2 = Hme #reset health
                        Ame2 = min(Ame2+B,100)#buff
                        Hme2 = Hme2 - 2*Ak2 #take damage
                        if (Hme2 <= 0):
                            moves = 50000
                            break
                        moves = moves + 2
                    else:
                        Ame2 = min(Ame2+B,100)#buff
                        Hme2 = Hme2 - Ak2 #take damage
                        moves = moves + 1
            if moves < 50000:
                while (Hk2>0 and moves < 1000):
                    if (Ak2 >= Hme):
                        moves = 50000
                        break
                    #elif (Ak2+Ak2>=Hme and Hk2 > 2*Ame2):
                    #    moves = 50000
                    #    break
                    elif (Ak2 >= Hme2):
                        if (Hk2 <= Ame2):
                            moves = moves+1
                            break
                        else:
                            Hme2 = Hme #reset health
                            Hk2 = Hk2 - Ame2
                            Hme2 = Hme2 - 2*Ak2 #take damage
                            if (Hme2 <= 0):
                                moves = 50000
                                break
                            else:
                                moves = moves + 2
                    else:
                        Hk2 = Hk2 - Ame2
                        Hme2 = Hme2 - Ak2 #take damage
                        moves = moves+1
            sol = min(moves,sol)
    if sol == 50000:
        print "Case #" + str(cc) +": "+"IMPOSSIBLE"
    else:
        print "Case #" + str(cc) +": "+str(sol)