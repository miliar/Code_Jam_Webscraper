def RangoN(numero):
    if numero<=30 and numero>=28:
       return 10
    elif numero<=27 and numero>=25:
       return 9
    elif numero<=24 and numero>=22:
       return 8
    elif numero<=21 and numero>=19:
       return 7
    elif numero<=18 and numero>=16:
       return 6
    elif numero<=15 and numero>=13:
       return 5
    elif numero<=12 and numero>=10:
       return 4
    elif numero<=9 and numero>=7:
       return 3
    elif numero<=6 and numero>=4:
       return 2
    elif numero<=3 and numero>=1:
       return 1
    elif numero==0:
       return 0
def Rango(numero):
    if numero<=30 and numero>=26:
        return 10
    elif numero<=27 and numero>=23:
        return 9
    elif numero<=24 and numero>=20:
        return 8
    elif numero<=21 and numero>=17:
        return 7
    elif numero<=18 and numero>=14:
        return 6
    elif numero<=15 and numero>=11:
        return 5
    elif numero<=12 and numero>=8:
        return 4
    elif numero<=9 and numero>=5:
        return 3
    elif numero<=6 and numero>=2:
        return 2
    elif numero<=3 and numero>=1:
        return 1
    elif numero==0:
        return 0
     


def Caso(Datos):
    i=3
    Sol=0
    No=0
    Array=Datos.split(' ') #Separa la cadena en cada uno de los elementos.
    tam=len(Array)#Numero de elementos en la cadena.
    #print(str(tam))
    p=int(Array[2])
    s=int(Array[1])
    #print(str(p))
    while i<=tam-1:
        numero=int(Array[i])
        totalizado=Rango(numero)
        NoSorprendente=RangoN(numero)
        #print("***"+str(totalizado)+"***"+str(NoSorprendente))
        if Rango(numero)>=p:
            Sol=Sol+1
        if RangoN(numero)>=p:
            No=No+1
        
        
        i=i+1
    #print("totales "+str(Sol)+" de los cuales")
    #print ("No sorprendetes "+str(No)+ "\nSorprendentes "+str(s))
    
    res=No+s
    if res>Sol:
        return Sol
    else:
        return res



def Solucion():
    Input=open('INPUT.txt','r')
    Output=open('OUTPUT.txt','w')
    #Leemos el primer renglon que sera T.
    T=Input.readline()
    w=int(T)
    tam=[]
    Datos=[]#Lista de cadenas.
    for i in range(w):
        Datos.append(Input.readline())
        tam.append(len(Datos[i]))
        #print ("Tamaño de la cadena" +str(tam[i]))
        #print (str(Datos[i])+"\n")

    #Solucionaremos para el caso Datos[0]
    i=0
    while i<=w-1:
     sol=Caso(Datos[i])#Contiene en la tercera posicion a P.
     print (str(sol))
     Output.write("Case #"+str(i+1)+": "+str(sol)+"\n")
     i=i+1
Solucion()
