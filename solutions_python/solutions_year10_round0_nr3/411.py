#!/usr/bin/env python
out = open('pep2e','w')
def resolver(r,k,grupos,j):
    corridas = 0
    ganancia=0
    aux = []
    while(corridas < r):
        acum = 0
        for each in range(len(grupos)):
            x = grupos.pop(0)
            
            if acum + x <= k:
                acum += x
                aux.append(x)
            else:
                grupos.insert(0,x)
                break
        corridas+=1

        ganancia+=acum
        grupos.extend(aux)

        aux = []
    out.write("Case #%s: %s\n"%(j,ganancia))
    
casos = int(raw_input())
j = 1
while(j <= casos):
    r,k,n = (int(x) for x in raw_input().split(" "))
    grupos = [int(x) for x in raw_input().split(" ")]

    
    
    resolver(r,k,grupos,j)
    j+=1

out.close()
    
    
    



