#-*- coding: utf-8 -*-

import sys
from datetime import time

class Evento:
    def __cmp__(self, other):
        if self.hora < other.hora:
            return -1
        elif self.hora == other.hora:
            if self.tipo == other.tipo:
                return 0
            if self.tipo == 'L':
                return -1
            return 1
        else:
            return 1
if __name__ == '__main__':
    file_name = sys.argv[1]

    input_file = open(file_name).readlines()
    output_file = open('output.ou', 'w')
    
    N = int(input_file[0])
    input_file = input_file[1:]

    for case in range(1, N+1):
        T = int(input_file[0])
        input_file = input_file[1:]

        NA, NB = input_file[0].split()
        NA = int(NA)
        NB = int(NB)
        
        input_file = input_file[1:]

        eventos = []
        estacion = 1
        for line in input_file[0:NA+NB]:
            salida, llegada = line.split()
            salida = time(int(salida.split(":")[0]),
                          int(salida.split(":")[1]))
            
            evento = Evento()
            evento.hora = salida
            evento.tipo = 'S'
            if estacion <= NA:
                evento.estacion = 'A'
            else:
                evento.estacion = 'B'
            eventos.append(evento)
            llegada = time(int(llegada.split(":")[0]),
                           int(llegada.split(":")[1]))
            #sumar el tiempo de giro

            if (llegada.minute + T) < 60:
                llegada = llegada.replace(llegada.hour,
                                          llegada.minute+T)
            else:
                if (llegada.hour +1) >= 24:
                    llegada = llegada.replace(23, 59)
                else:
                    llegada = llegada.replace(llegada.hour + 1,
                                              T-(60-llegada.minute))
            evento = Evento()
            evento.hora = llegada
            evento.tipo = 'L'
            
            if estacion <= NA: 
                evento.estacion = 'B'
            else:
                evento.estacion = 'A'
            eventos.append(evento)

            estacion += 1

        input_file = input_file[NA+NB:]
  #      for evento in eventos:
   #         print evento.hora, " ", evento.tipo, " ", evento.estacion, "\n"


        eventos.sort()

#        for evento in eventos:
 #           print evento.hora, " ", evento.tipo, " ", evento.estacion


        ta = na = tb = nb = 0  #t-trenes n-necesidad a,b-estacion

        for evento in eventos:
            if evento.tipo == 'S': #una salida de tren
                if evento.estacion == 'A':
                    if ta == 0:
                        na += 1
                    else:
                        ta -= 1
                else:
                    if tb == 0:
                        nb += 1
                    else:
                        tb -= 1
            else: # una llegada
                if evento.estacion == 'A':
                    ta += 1
                else:
                    tb += 1
 
        output_file.write("Case #%d: %d %d\n"%(case, na, nb))
