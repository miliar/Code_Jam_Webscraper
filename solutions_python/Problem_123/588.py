# -*- coding: utf-8 -*-
## Problema D
#import itertools

input = open('C:\Users\Luis\Desktop\CODE JAM\A-small-attempt2.in', 'r')

output = open('C:\Users\Luis\Desktop\CODE JAM\output_2_A.txt', 'w')

casos=int(input.readline())

for i in range(casos):#Volver a poner "casos"
    
    #LEO DATOS
    linea1=input.readline().split()
    size=int(linea1[0])
    sizeini=size
    numbolas=int(linea1[1])
   
    linea2=input.readline().split()
    bolas=[]
    for j in range(numbolas):
        bolas.append(int(linea2[j]))
    bolas.sort()
    
     
     
     
    #EMPIEZO RESOLUCION
    operaciones=0
    fin=0
    for b in range(numbolas):
        if fin==0:
            if bolas[b]<size:
                size=size+bolas[b]
            else:
                if bolas[b]<(2*size-1):
                    size=2*size-1+bolas[b]
                    operaciones=operaciones+1
                else:
                    #if b>(numbolas-4):
                    #    operaciones=operaciones+2
                    #    fin=1
                    
                    #algoritmo complicado
                    maxoperaciones=numbolas-b
                    hecho=0
                    index=0
                    while hecho==0:
                        index=index+1
                        if index>=maxoperaciones:
                            fin=1
                            operaciones=operaciones+maxoperaciones
                            hecho=1
                        else:
                            size=2*size-1
                            if size>bolas[b]:
                                hecho=1
                                operaciones=operaciones+index
                                size=size+bolas[b]
    print i,sizeini,bolas,operaciones    
                        
        
                
    
          
 
        
            
    output.write('Case #{0}: {1}\n'.format(i+1,operaciones))
print "FIN"


       

input.close()
output.close()
