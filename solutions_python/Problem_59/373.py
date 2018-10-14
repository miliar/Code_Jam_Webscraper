#! /usr/bin/python

from string import split
import sys

__author__ = "Guillermo Candia Huerta"
__date__ = "$22-05-2010 11:51:49 AM$"

def resolver():
    input_file = sys.argv[1]
    output_file = input_file.replace('.in', '.out', 1)

    input = open(input_file, 'r')
    output = open(output_file, 'w')

    cases = int(input.readline())

    
    
    for c in range(0, cases):
        output.write('Case #' + str(c + 1) + ': ')

        #comienza resolucion
        directorios = []
        mk = 0
        
        linea = map(int, input.readline().split())
        N = linea[0]
        M = linea[1]

        for d in range(0, N):
            linea = input.readline().strip()
            s = linea.count('/')
            while s > 0:
                if linea not in directorios:
                    directorios.append(linea)
                linea = linea[:linea.rindex('/')]
                s -= 1
        for d in range(0, M):
            linea = input.readline().strip()
            s = linea.count('/')

            while s > 0:
                if linea not in directorios:
                    directorios.append(linea)
                    mk += 1
                linea = linea[:linea.rindex('/')]
                s -= 1

        output.write(str(mk))

        #termina resolucion

        output.write('\n')
    input.close()
    output.close()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print 'Use: ./' + split(sys.argv[0], '/')[-1] + ' input_file'
    else:
        resolver()
