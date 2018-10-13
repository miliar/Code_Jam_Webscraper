def leerarchivo(nombredelarchivo):
    archivo=open(x,'r')
    archivo=archivo.read()
    archivo=archivo.split()
    for i in range(len(archivo)):
        archivo[i]=int(archivo[i])
    return archivo

def imprimirdato(y,respuesta,numcase):
    
    archivo=open(y,"w")
    archivo.write(respuesta+"\n")
    archivo.close()

x=raw_input()
y= 'respuestas2.txt'

lista=leerarchivo(x)
numerosort=[]
numero=[]
numtests=lista[0]
numcase=1
imprimir=''
respuesta=''
mayor=0
for i in range(1,(numtests+1)):
    
    numeros=[int(j) for j in str(lista[i])]
    mayor=''.join(str(numeros[0]) for i in range(len(numeros)))
    mayor=int(mayor)
     
        
    if mayor > lista[i]:
        
        for i in range(1,len(numeros)):
            numeros[i]=0
    if len(numeros)==1:
        imprimir=''.join(str(l) for l in numeros)
        respuesta="Case #"+str(numcase)+": "+imprimir
        print respuesta
        #imprimirdato(y,respuesta,numcase)
    
        
    else:
        counter=(len(numeros)-1)
        while(0==0):
            numerosort=numeros[:]
            numerosort.sort()
            if numeros==numerosort:
                if numeros[0]==0:
                    numeros.pop(0)
                imprimir=''.join(str(l) for l in numeros)
                respuesta="Case #"+str(numcase)+": "+imprimir
                print respuesta
                #imprimirdato(y,respuesta,numcase)
                break
            
                       
                       
            if counter >= 0:
                if numeros[counter] <= numeros[counter-1]:
                    numeros[counter]=9
                    numeros[counter-1]-=1
                    counter-=1
                else:
                    counter-=1
            if numeros[0]==0:
                numeros.pop(0)
            
            
            
        
    
    
    numcase+=1
