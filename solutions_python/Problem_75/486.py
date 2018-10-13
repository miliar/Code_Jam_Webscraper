
import sys




T=int(sys.stdin.readline())



    
   
for i in range(0,T):
    bases={}
    pairs=[]
    tk=sys.stdin.readline().split()
    tk.reverse()
    C=int(tk.pop())
    for j in range(0,C):
        production=tk.pop()
        bases[production[0:2]]=production[2]
    D=int(tk.pop())
    for j in range(0,D):
        pair=tk.pop()
        pairs.append(pair)
    N=int(tk.pop())
    sequence=tk.pop()
    resultado=[]
    apariciones={'Q':0, 'W':0, 'E':0, 'R':0, 'A':0, 'S':0, 'D':0, 'F':0}
    for k in range(0,N):
        flag=0
        if (len(resultado)>0):
            anterior=resultado[-1]
            for key in bases:
                if (key==(sequence[k]+anterior) or key==(anterior+sequence[k])):
                    apariciones[anterior]-=1
                    resultado.pop()
                    resultado.append(bases[key])
                    flag=1
                    break
        if flag==0:
            for pp in pairs:
                if (pp[0]==sequence[k]):
                    if (apariciones[pp[1]]>0):
                        resultado=[]
                        apariciones={'Q':0, 'W':0, 'E':0, 'R':0, 'A':0, 'S':0, 'D':0, 'F':0}
                        flag=1
                        break
                elif (pp[1]==sequence[k]):
                    if (apariciones[pp[0]]>0):
                        resultado=[]
                        apariciones={'Q':0, 'W':0, 'E':0, 'R':0, 'A':0, 'S':0, 'D':0, 'F':0}
                        flag=1
                        break
        if flag==0:
            resultado.append(sequence[k])
            apariciones[sequence[k]]+=1
    cadena='['
    if resultado:
        cadena+=resultado[0]
        for u in range(1,len(resultado)):
            cadena+=', '+str(resultado[u])
        cadena+=']'
    else:
        cadena='[]'
    
    print 'Case #'+str(i+1)+': '+cadena
         
