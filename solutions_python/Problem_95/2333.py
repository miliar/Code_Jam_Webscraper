# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
fn = 'A.in'
#-------------------------------------------------------------------------------
def correr_tarea(tarea):
#   Algoritmo
    resp = ''
    convmap = [['a','y'],['b','h'],['c','e'],['d','s'],['e','o'],['f','c']
    ,['g','v'],['h','x'],['i','d'],['j','u'],['k','i'],['l','g'],['m','l']
    ,['n','b'],['o','k'],['p','r'],['q','z'],['r','t'],['s','n'],['t','w']
    ,['u','j'],['v','p'],['w','f'],['x','m'],['y','a'],['z','q']]
    for word in tarea:
        gglword = ''
        for i in range(len(word)):
            gglword += convmap[ord(word[i])-97][1]
        resp += ' ' + gglword
    return resp.strip()
#-------------------------------------------------------------------------------      
def leer_entrada_1():
    """2 T 
       5 N 
       1 2 3 4 5 N  numeros
       3
       3 5 6"""
    linea = str.split(entrada.readline())
    return correr_tarea(linea)
#-------------------------------------------------------------------------------
def leer_entrada_2():
    """ Input
3
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv


Output
Case #1: our language is impossible to understand
Case #2: there are twenty six factorial possibilities
Case #3: so it is okay if you want to just give up"""
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