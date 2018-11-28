import random

def iniciar():
    archivo = open("ej.txt", "r") 
    t = archivo.readline()
    t = int(t)
    for i in range(1, t+1):
        ej = archivo.readline()
        result = resolver(ej)
        print "Case #" + str(i) + ": " + str(result)

def resolver(ej):
    c = ej.split(" ")[0] 
    k = ej.split(" ")[1] 

    # print c
    # print k
    c = list(c)
    k = int(k)
    cambios = 0
    while len(c) >= k:
        # print c
        # print cambios
        if c[0] == "-":
            cambios = cambios + 1
            for i in xrange(0,k):
                if c[i] == "+":
                    c[i] = "-"
                else:
                    c[i] = "+"
        c= c[1:]
    if "-" in c:
        return "IMPOSSIBLE"
    else:
        return cambios

iniciar() 
