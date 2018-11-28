import string
import math

input = 'A-large.in'
output = 'output-a-large'
try:
    f = open(input, 'r')
except:
    exit('file: ' + input + ' non trovato')
try:
    out = open(output, 'w')
except:
    exit('file: ' + output + ' non trovato')

N = int(f.readline())

for k in range(N):
    l1 = f.readline()
    l2 = string.split(l1)
    M = int(l2[0])
    del l2[0]
    l3 = []
    i = 0
    while i < len(l2):
        l3.append([l2[i], int(l2[i + 1])])
        i = i + 2
        
    hash = {'O':0, 'B':0}
    pos = {'O':1, 'B':1}
    prec = 'O'
    time = 0
    for x in l3:
        mov = abs(pos[x[0]] - x[1])
        if prec != x[0]:
            mov = mov - hash[prec]
            if mov < 0:
                mov = 0
            hash[prec] = 0
        time = time + mov + 1
        pos[x[0]] = x[1]
        hash[x[0]] = hash[x[0]] + mov + 1
        prec = x[0]
    
    print time
    out.write('Case #' + str(k + 1) + ': ' + str(time) + '\n')
