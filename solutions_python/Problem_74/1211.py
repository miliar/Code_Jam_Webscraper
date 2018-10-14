#! /usr/bin/python

from string import split
import sys

__author__="Guillermo Candia Huerta"
__date__ ="$06-05-2011 11:08:08 PM$"

def resolver(e):
    r = 0

    posicionO = 1
    posicionB = 1

    tiempoO = 0
    tiempoB = 0

    for i in range(1, int(e[0]) * 2, 2):
        if e[i] == 'O':
            tiempo_necesario = abs(int(e[i+1]) - posicionO) + 1

            if tiempo_necesario <= tiempoO:
                r = r + 1
                tiempoB = tiempoB + 1
            else:
                r = r + tiempo_necesario - tiempoO
                tiempoB = tiempoB + tiempo_necesario -tiempoO
            tiempoO = 0
            posicionO = int(e[i+1])

        if e[i] == 'B':
            tiempo_necesario = abs(int(e[i+1]) - posicionB) + 1

            if tiempo_necesario <= tiempoB:
                r = r + 1
                tiempoO = tiempoO + 1
            else:
                r = r + tiempo_necesario - tiempoB
                tiempoO = tiempoO + tiempo_necesario -tiempoB
            tiempoB = 0
            posicionB = int(e[i+1])

    
    return str(r)
    

if __name__ == "__main__":
#    if len(sys.argv) == 1:
#        print 'Use: ./' + split(sys.argv[0], '/')[-1] + ' input_file'
#    else:
#        input_file = sys.argv[1]

#    input_file = "A-test.in"
#    input_file = "A-small-attempt0.in"
    input_file = "A-large.in"

    output_file = input_file.replace('.in', '.out', 1)

    input = open(input_file, 'r')
    output = open(output_file, 'w')

    cases = int(input.readline())

    for c in range(0, cases):
        output.write('Case #' + str(c+1) + ': ' + resolver(input.readline().split()) + '\n')
    input.close()
    output.close()

