# -*- coding: cp1252 -*-
#Alexander Pinzon
#Python 2.5
#Español

class motor:
    def __init__(self, unos_engines):
        self.num = len(unos_engines)
        self.motor = unos_engines
        self.cambios = 0
        
    def busquedaMasLarga(self, palabras):
        if (len(palabras)<=1):
            return []
        n = 0
        q = 0
        usado = []
        for i in range(self.num):
            usado.append(False)
        while(n<self.num and q <len(palabras)):
            indice = self.motor.index(palabras[q])
            if (usado[indice] == False):
                n = n + 1
                usado[indice] = True
            else:
                usado[indice] = True
            q = q + 1
        if(q < len(palabras)):
            self.cambios = self.cambios + 1
            return palabras[q-1:]
        else:
            if (n >=self.num):
                self.cambios = self.cambios + 1
        return []
    def busquedaMasLarga2(self, palabras):
        cadena = palabras
        while( cadena <> []):
            cadena = self.busquedaMasLarga(cadena)
        return self.cambios
        
                
def readInput(path_file_input, path_file_output):
    myFileIn = open(path_file_input, "r")
    myFileOut = open(path_file_output, "w")
    lines = myFileIn.readlines()
    myFileIn.close() 
    N = int((lines[0].split("\n"))[0])
    i = 1
    linea = 1
    while(i<N+1):
        S = int((lines[linea].split("\n"))[0])
        linea = linea +1
        motors = []
        for j in range(linea, linea+S):
            motors.append((lines[j].split("\n"))[0])
        Q = int((lines[linea+S].split("\n"))[0])
        linea = linea +1
        busquedas = []
        for j in range(linea+S, linea+S+Q):
            busquedas.append((lines[j].split("\n"))[0])
        M = motor(motors)
        Y = M.busquedaMasLarga2(busquedas)
        case = "Case #" + str(i) + ": " + str(Y) + "\n"
        myFileOut.write(case)
        linea = linea+S+Q
        i = i + 1
    myFileOut.close()    

path_file_input = input("Input file path: (sample use 'x:/path/file.input'):  ")
path_file_output = input("Output file path: (sample use 'x:/path/file.output'):  ")
readInput(path_file_input, path_file_output)
print "OK"
