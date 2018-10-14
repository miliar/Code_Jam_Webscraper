# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
fn = 'C.in'
#-------------------------------------------------------------------------------
def correr_tarea(tarea):
#   Algoritmo
    resp = ''

    return resp.strip()
#-------------------------------------------------------------------------------      
def leer_entrada_1():
    """2 T 
       5 N 
       1 2 3 4 5 N  numeros
       3
       3 5 6"""
    A, B = map(int,str.split(entrada.readline()))
    test = ''
    recicledpairsfound = 0
    for i in range(A,B+1):
        test = str(i)
        if (len(test) > 1):
            swapped = 0
            for j in range(1,len(test)):
                swapped = int(test[-j:] + test[:len(test)-j])
                if (i < swapped <= B):
                    recicledpairsfound += 1
                    #print 'A: %s B: %s i: %s cadena: %s, casos: %s' %(A,B,i,swapped,recicledpairsfound)
            
    return recicledpairsfound
#-------------------------------------------------------------------------------
def leer_entrada_2():
    """Input
4
1 9
10 40
100 500
1111 2222
Output
Case #1: 0
Case #2: 3
Case #3: 156
Case #4: 287
"""
    var1 = int(entrada.readline())
    var2 = int(entrada.readline())
    lista = []
    for i in xrange(1,var2):
        lista = lista + [map(int,str.split(entrada.readline()))]   
    return correr_tarea(var1,var2,lista)
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
 
entrada = open(fn,'r')
salida = open(fn[:-3] + '.out','w')
casos = int(entrada.readline())
for caso in range(casos):
    Ans = leer_entrada_1()
    salida.write('Case #%s: %s\n' % (caso + 1, Ans))
entrada.close();salida.close()