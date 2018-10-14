__author__ = 'sisekeom'

from sys import argv

def improves(nF,C,X,F):
    current = X/(2+(nF*F))
    possibility = C/(2+nF*F) + X/(2+(nF+1)*F)
#    print(current)
#    print(possibility)
    return possibility < current


if __name__=="__main__":
    nombre = open(argv[1],'r')
    n = int(nombre.readline())
    for i in range(n):
        line = nombre.readline().strip().split(" ")
        nF = 0
        nFpre = -1
        C = float(line[0])
        F = float(line[1])
        X = float(line[2])

        while nF != nFpre:
            nFpre = nF
            if improves(nF,C,X,F):
                nF=nF+1
        result = 0
        for j in range(nF):
            result = result+(C/(2+(j*F)))
        result = result + (X/(2+(nF*F)))
        print("Case #{0}: {1}".format(i+1,result))