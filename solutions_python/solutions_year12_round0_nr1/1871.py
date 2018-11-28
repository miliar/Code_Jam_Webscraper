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
        print ("Tamaño de la cadena" +str(tam[i]))
        print (str(Datos[i])+"\n")
    j=0
    #Para el caso 0. Podemos anidar un while.
    while j<=w-1:
        Caso(j,Datos,tam,Output)
        j=j+1
    
def Caso(numero,Datos,tam,Output):
      i=numero
      j=0
      Cadena_aux=str(Datos[i])
      Lista_aux=[]
      while j<=tam[i]-1:
        
          letra=Cadena_aux[j]
          
          if   letra=='a':
                Lista_aux.append('y')
          elif letra=='b':
                Lista_aux.append('h')
          elif letra=='c':
                Lista_aux.append('e')
          elif letra=='d':
                Lista_aux.append('s')
          elif letra=='e':
                Lista_aux.append('o')
          elif letra=='f':
                Lista_aux.append('c')
          elif letra=='g':
                Lista_aux.append('v')
          elif letra=='h':
                Lista_aux.append('x')
          elif letra=='i':
                Lista_aux.append('d')
          elif letra=='j':
                Lista_aux.append('u')
          elif letra=='k':
                Lista_aux.append('i')
          elif letra=='l':
                Lista_aux.append('g')
          elif letra=='m':
                Lista_aux.append('l')
          elif letra=='n':
                Lista_aux.append('b')
          elif letra=='o':
                Lista_aux.append('k')
          elif letra=='p':
                Lista_aux.append('r')
          elif letra=='q':
                Lista_aux.append('z')
          elif letra=='r':
                Lista_aux.append('t')
          elif letra=='s':
                Lista_aux.append('n')
          elif letra=='t':
                Lista_aux.append('w')
          elif letra=='u':
                Lista_aux.append('j')
          elif letra=='v':
                Lista_aux.append('p')
          elif letra=='w':
                Lista_aux.append('f')
          elif letra=='x':
                Lista_aux.append('m')
          elif letra=='y':
                Lista_aux.append('a')
          elif letra=='z':
                Lista_aux.append('q')
          elif letra==' ':
                Lista_aux.append(' ')
          j=j+1
      FinalString=''.join(Lista_aux)
      print (FinalString)
      Output.write("Case #"+str(i+1)+": "+str(FinalString)+"\n")
     
              
        
Solucion()
