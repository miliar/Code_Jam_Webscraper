# -*- coding: cp1252 -*-
#Alexander Pinzon
#Python 2.5
#Español

class Hora:
    def __init__(self, una_hora=0, un_min=0):
        if (isinstance(una_hora,int) ):
            self.min = (una_hora * 60 + un_min )%1440
        elif (isinstance(una_hora,str) ):
            temp = una_hora.split(":")
            hora = int(temp[0])
            minu = int(temp[1])
            self.min = (hora * 60 + minu )%1440
        else:
            self.min = 0
    def __add__(self, x):
        m = self.min + x.min
        return  Hora(0,m)
    def __radd__(self,x):
        m = self.min + x.min
        return  Hora(0,m)
    def __sub__(self,x):
        m = self.min - x.min
        return  Hora(0,m)
    def __rsub__(self,x):
        m = x.min - self.min
        return  Hora(0,m)
    def __neg__(self):
        m = -self.min
        return  Hora(0,m)
    def getHora(self):
        return int(self.min/60)
    def getMin(self):
        return self.min%60
    def __cmp__(self, x):
        c = 0
        if (self.min < x.min):
            c = -1
        elif(self.min > x.min):
            c = 1
        return c
    def __str__(self):
        cad = str(self.getHora()) + ":" + str(self.getMin())
        return cad
    def __repr__(self):
        cad = str(self.getHora()) + ":" + str(self.getMin())
        return cad
        
class Tren:
    def __init__(self, un_puerto, una_hora, un_enSalida = True):
        #puerto A B
        self.puerto = un_puerto
        #si no esta en la entrada entonces en la salida
        self.enSalida = un_enSalida
        self.hora = una_hora
    def __str__(self):
        cad = "Tren: " + str(self.puerto) + " " +str(self.hora)
        return cad
    def __repr__(self):
        cad = "Tren: " + str(self.puerto) + " " +str(self.hora)
        return cad
    
class Trans:
    def __init__(self, un_T, un_NA, un_NB, unas_lineas):
        self.T = Hora(0,un_T)
        self.NA = un_NA
        self.NB = un_NB
        self.viajes = []
        self.viajes = []
        self.SalenDeA = 0
        self.SalenDeB = 0
        for i in range(self.NA):
            htemp = (unas_lineas[i].split("\n")[0]).split(" ")
            viaje = []
            viaje.append(Hora(htemp[0]))
            viaje.append(Hora(htemp[1]))
            viaje.append("A")
            self.viajes.append(viaje)
        for i in range(self.NA, self.NA + self.NB):
            htemp = (unas_lineas[i].split("\n")[0]).split(" ")
            viaje = []
            viaje.append(Hora(htemp[0]))
            viaje.append(Hora(htemp[1]))
            viaje.append("B")
            self.viajes.append(viaje)
        #Order hour's for first element in each tripla, with my compare function(__cmp__) of Hora class
        self.viajes.sort()
        self.trenes = []
    def HayTren(self, un_viaje):
        n = 0
        k = -1
        while(n<len(self.trenes)):
            t = self.trenes[n]
            if (t.puerto == un_viaje[2]):
                if(t.enSalida) :
                    thora = t.hora
                else:
                    thora = self.T + t.hora
                if (thora<=un_viaje[0]):
                    k = n
                    n = len(self.trenes)
            n = n + 1
        return k
    def run(self):
        for v in self.viajes:
            tren_numero = self.HayTren(v)
            if (tren_numero<> -1):
                mi_tren = self.trenes[tren_numero]
                if(v[2] == "A"):
                    mi_tren.puerto = "B"
                else:
                    mi_tren.puerto = "A"
                mi_tren.hora = v[1]
                mi_tren.enSalida = False
            else:
                if(v[2] == "A"):
                    self.SalenDeA = self.SalenDeA + 1
                    mi_puerto = "B"
                else:
                    self.SalenDeB = self.SalenDeB + 1
                    mi_puerto = "A"
                mi_tren = Tren(mi_puerto, v[1], False)
                self.trenes.append(mi_tren)
                
def readInput(path_file_input, path_file_output):
    myFileIn = open(path_file_input, "r")
    myFileOut = open(path_file_output, "w")
    lines = myFileIn.readlines()
    myFileIn.close() 
    N = int((lines[0].split("\n"))[0])
    i = 1
    linea = 1
    while(i<N+1):
        T = int((lines[linea].split("\n"))[0])
        linea = linea +1
        naYnb = ((lines[linea].split("\n"))[0]).split(" ")
        NA = int(naYnb[0])
        NB = int(naYnb[1])
        linea = linea +1
        lineasViajes = lines[linea:linea+NA+NB]
        linea = linea+NA+NB
        x = Trans(T,NA,NB, lineasViajes)
        x.run()
        case = "Case #" + str(i) + ": " + str(x.SalenDeA) + " " + str(x.SalenDeB) + "\n"
        myFileOut.write(case)
        i = i + 1
    myFileOut.close()    

path_file_input = input("Input file path: (sample use 'x:/path/file.input'):  ")
path_file_output = input("Output file path: (sample use 'x:/path/file.output'):  ")
readInput(path_file_input, path_file_output)
print "OK"
