# -*- coding: utf-8 -*-
import math


casos = int(input(""))
i = 0
mensajes = []
while i<casos:
    valor = input("")
    valor = valor[2:] 
    timido=0
    total=0
    agregados=0
    while timido+1<len(valor):
        total+=int(valor[timido])
        if total<(timido+1):
            agregados+=(timido+1)-total
            total+=(timido+1)-total
        timido+=1
    mensajes.append("Case #"+str(i+1)+": "+str(agregados))
    i+=1

            

n=0
while n<len(mensajes):
    print(mensajes[n])
    n+=1