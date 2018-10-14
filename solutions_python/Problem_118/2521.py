import sys
class Logger(object):
        def __init__(self, filename="Default.log"):
            self.terminal = sys.stdout
            self.log = open(filename, "a")

        def write(self, message):
            self.terminal.write(message)
            self.log.write(message)
sys.stdout = Logger("resultat.txt")

from math import sqrt
def palind(N):
            k=0
            T=True
            chN=str(N)
            l=len(chN)
            while ((k < l/2) and (T==True)):
                if (chN[k]==chN[l-k-1]):
                    k+=1
                else:
                    return False
            return T

def jeu():
    fichier = open("C:\Users\PC\Downloads\C-small-attempt0.in", 'r')
    n=fichier.readline()
    n=int(n)
    
    for i in range(n):
        ch=fichier.readline()
        L=ch.split(' ')
        Nb=0
        A=L[0]
        B=L[1]
        A=int(A)
        B=int(B)
        for j in range(A,B+1):
            if (palind(j)):
                j2=sqrt(j)
                if (j2==int(j2)):
                    j2=int(j2)
                    if (palind(j2)):
                        Nb+=1
        rs="Case #"+str(i+1)+": "+str(Nb)
        print rs
jeu()

