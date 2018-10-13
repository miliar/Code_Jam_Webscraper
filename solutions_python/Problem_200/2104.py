import random

def iniciar():
    archivo = open("ej.txt", "r") 
    t = archivo.readline()
    t = int(t)
    for i in range(1, t+1):
        ej = archivo.readline().strip()
        result = resolver(ej)
        print "Case #" + str(i) + ": " + str(result)

def resolver(ej):
    ej = list(ej)
    i = len(ej) - 1
    j = len(ej) - 2 
    while j >= 0:
        if ej[j] > ej[j+1]:
            ej[j] = str(int(ej[j])-1)
            for k in xrange(j+1,i+1):
                ej[k] = "9"
            i = j
        j = j - 1

    return int(''.join(ej))

iniciar() 
