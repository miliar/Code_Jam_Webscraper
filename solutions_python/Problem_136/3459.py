'''
Created on 12/04/2014

@author: luis
'''
import sys
sys.setrecursionlimit(100000)

class Case():
    def __init__(self, caso, C, F, X):
        self.caso = int(caso)+1
        self.costeF = C
        self.acumulador = F
        self.CookiesPorSegundo = 2
        self.objetivo = X

    def tHastaSiguienteF(self):
        return float(self.costeF/self.CookiesPorSegundo)

    def tHastaX(self,aumento):
        return float(self.objetivo/float(aumento))

    def resuelve(self, tActual):
        tiempoConUnaFMas = tActual + self.tHastaSiguienteF()+ self.tHastaX(self.CookiesPorSegundo+self.acumulador)
        tiempoAhora = tActual + self.tHastaX(self.CookiesPorSegundo)
        if (tiempoConUnaFMas) > (tiempoAhora):
            outfile.write("Case #"+str(self.caso)+": %s \n" % "{0:.7f}".format(tiempoAhora))
        else:
            #buy a new Farm
            tActual = tActual + self.tHastaSiguienteF()
            self.CookiesPorSegundo = self.CookiesPorSegundo+self.acumulador
            return self.resuelve(tActual)

infile = open('B-small-attempt2.in', 'r')
outfile = open('output.txt', 'w')
caseNumbers = int(infile.readline())
for i in range(caseNumbers):
    linea = infile.readline().split()
    caso = Case(i, float(linea[0]), float(linea[1]), float(linea[2]))
    caso.resuelve(0)

infile.close()
outfile.close()