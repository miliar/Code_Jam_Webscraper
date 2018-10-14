# -*- coding: utf-8 -*-
## Problema C

def pal(a):
    try:
        a=str(a)
        tam=len(a)
        palin=1
        if a[tam-1]=='0':
            palin=0
        if palin==1:
            for j in range(tam/2):
                if a[j]!=a[tam-1-j]:
                    palin=0
                    break
        if palin==1:
            return 1
        else:
            return 0

    except:
        print 'Error en funcion pal'
        pass


input = open('C:\Users\Luis\Desktop\CODE JAM\C-small-attempt0.in', 'r')

output = open('C:\Users\Luis\Desktop\CODE JAM\output1small.txt', 'w')

casos=int(input.readline())

for i in range(casos):
    linea=input.readline().split()
    a=int(linea[0])
    b=int(linea[1])
    resultado=0
    while a<=b:
        #compruebo que es el cuadrado de un entero
        if int(a**0.5)**2==a:
            #compruebo que el pequeño es palindromo
            if pal(int(a**0.5))==1:
                #compruebo que el grande es palindromo
                if pal(a)==1:
                    resultado+=1
        a+=1
    
    print resultado
            
    output.write('Case #{0}: {1}\n'.format(i+1,resultado))


            
        



input.close()
output.close()

#line = f.readline()