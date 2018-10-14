casos = []
T = input()
for i in range(T):
    casos.append(raw_input())


i = 0
j = 0
k = 0

for k in range(len(casos)):
    numero=int(casos[k])
    lista=list(str(numero))
    if(len(lista)==1):
        orden = 'Case #'+ str(k+1) +": "+ str(numero)
        print orden
    else:
        i=0
        while(i+1<len(lista)):
            if int(lista[i+1]) < int(lista[i]):
                numero=numero-1
                lista=list(str(numero))
            else:
                i=i+1
        j=0
        while(j+1<len(lista)):
            if(int(lista[j+1]) < int(lista[j])):
                numero=numero-1
                lista=list(str(numero))
            else:
                j=j+1
        resultado = 'Case #'+ str(k+1) +": "+ str(numero)
        print resultado