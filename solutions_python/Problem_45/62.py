#! /usr/bin/python
import sys

def permuts(seznam):
    if len(seznam) <=1:
        yield seznam
    else:
        for permut in permuts(seznam[1:]):
            for i in range(len(permut)+1):
                yield permut[:i] + seznam[0:1] + permut[i:]


cases = int(sys.stdin.readline()[:-1])
actual_case = 0

while actual_case < cases:
    # reading and so
    actual_case += 1
    #nacteni 1 cisla
    
    #nacteni 2 cisel
    numbers = sys.stdin.readline()[:-1].split()
    pp = int(numbers[0])
    qq = int(numbers[1])

    #nacitani cisel v radku do promenne
    line = sys.stdin.readline()[:-1].split()
    list = []
    for i in range(qq):
        list.append(int(line[i]))

    cells = range(pp)
    for i in range(pp):
        cells[i] = 1
    
    min_bribes = (pp+1)*(qq+1)
    for permut in permuts(list):
        bribes = 0
        for i in range(qq):
            cela = permut[i] - 1
            tam = cela + 1
            zpet = cela - 1
            cells[cela] = 0
            while (tam < pp) and (cells[tam]):
                bribes += 1
                tam += 1
            while (zpet >= 0) and (cells[zpet]):
                bribes += 1
                zpet -= 1
        for i in range(qq):
            cells[permut[i] - 1] = 1
        if bribes < min_bribes:
            min_bribes = bribes
    
    print "Case #%d: %d" %(actual_case,min_bribes)
