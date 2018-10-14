# -*- coding: utf-8 -*-
fname = 'C-large'
f1 = open(fname + '.in','r')
f2 = open(fname + '.out','w')
Testcases = int(f1.readline())
"Bucle de operaciones"

for case in range(Testcases):
    Resultado = ''
    candies = int(f1.readline())
    bag = map(int,str.split(f1.readline()))
    bag.sort()
    tst = 0
    for i in range(len(bag),0,-1):
        tst = tst ^ bag[-i]
    if tst <> 0:
        Resultado = 'NO'
    else:
        Resultado = str(sum(bag[1:]))
    f2.write('Case #%s: %s\n' % (case + 1, Resultado))
f1.close();f2.close()