#!/usr/bin/python

fname = "data.in"
fin = open(fname)
i = 0
with fin as f:
    content = f.readlines()

albero = {}
for l in content:
    if i > 0:
        lista = l.rstrip("\n").split(" ")
        amici = 0
        numeri = list(lista[1])
        n = 0
        credito = -1
        while n < len(numeri):
            credito = credito + int(numeri[n])
            if credito - n < 0:
                credito = credito + 1
                amici = amici + 1
            n = n + 1



        print "Case #"+str(i)+": "+str(amici)

    i += 1


fin.close()
#out.close()
