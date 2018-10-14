#!/usr/bin/env python

import math

inf = open("in.txt", "r")
outf = open("out.txt", "w")

count = int(inf.readline())
j=0

for i in range(1, count + 1):
    print "caso", i
    j += 1
    line = inf.readline()[:-1]
    tareas = line.split()
    tareas.pop(0)

    O = 1
    B = 1

    tiempo=0
    Oacum=0
    Bacum=0
    while len(tareas) > 0:
        robot=tareas.pop(0)
        movimiento=tareas.pop(0)
        print "mov:", movimiento
        if robot == "O":
            if Bacum==0:
                tiempo += abs(int(movimiento) - O) + 1
                Oacum += abs(int(movimiento) - O) + 1
            else:
                if (abs(int(movimiento) - O) - Bacum) > 0:
                    tiempo += (abs(int(movimiento) - O) - Bacum) + 1
                    Oacum += (abs(int(movimiento) - O) - Bacum ) + 1
                else:
                    tiempo += 1
                    Oacum += 1
                         
            Bacum = 0
            O = int(movimiento)
        else:
            if Oacum==0:
                tiempo += abs(int(movimiento) - B) + 1
                Bacum += abs(int(movimiento) - B) + 1
            else:
                if (abs(int(movimiento) - B) - Oacum) > 0:
                    tiempo += (abs(int(movimiento) - B) - Oacum) + 1
                    Bacum += (abs(int(movimiento) - B) - Oacum) + 1
                else:
                    tiempo += 1
                    Bacum += 1        
            Oacum = 0
            B = int(movimiento)
        print "tiempo =",tiempo
    outf.write("Case #" + str(j) + ": " + str(tiempo) + "\n")
    print
print "listo si esto es igual a 0, esto =",len(inf.readline())
