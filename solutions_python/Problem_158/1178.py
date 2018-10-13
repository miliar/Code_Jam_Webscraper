# -*- coding: utf-8 -*-
import math


casos = int(input(""))
i = 0
mensajes = []
while i<casos:
    datos = input("")
    n=0
    temporal=""
    lista =[]
    lista2=[]
    while n<len(datos):
        if n==len(datos)-1:
            temporal +=datos[n]
            lista.append(temporal)
        if datos[n]==" ":
            if temporal!="":
                lista.append(temporal)
                temporal=""
        else:
            temporal +=datos[n]
        n+=1
    m=0
    while m<len(lista):
        lista2.append(int(lista[m]))
        m+=1
    minimo = round(lista2[0]/2)
    minimo2= minimo
    if minimo==(lista2[0]/2):
        minimo2=minimo+1
    if (lista2[2]*lista2[1])%lista2[0]!=0:
        mensajes.append("RICHARD")
    elif lista2[0]>lista2[1] and lista2[0]>lista2[2]:
        mensajes.append("RICHARD")
    elif (minimo>lista2[1] and minimo2>lista2[1]) or (minimo>lista2[2] and minimo2>lista2[2]):
        mensajes.append("RICHARD")
    elif (minimo==lista2[1] or minimo==lista2[2]) and lista2[0]>3:
        mensajes.append("RICHARD")
    else:
        mensajes.append("GABRIEL")
    i+=1
            
        
p=0
while p<len(mensajes):
    print("Case #"+str(p+1)+": "+mensajes[p])
    p+=1
