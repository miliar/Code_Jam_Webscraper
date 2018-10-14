def tidyest_number(N):
    if len(str(N))==1:
        return N
    while is_N_tidy(N)==False:
        N-=1
    return N

def is_N_tidy(N):
    L=[int(i) for i in str(N)]
    for k in range(len(str(N))-1):
        if L[k]>L[k+1]:
            return False
    return True

def what_to_write(t,N):
    answer=str(tidyest_number(int(N)))
    return "Case #"+str(t)+": "+answer

fichier=open("/home/quentin/Téléchargements/B-small-attempt1","r")
sortie=open("/home/quentin/Téléchargements/pb2-small-output","w")
liste=''.join(fichier)
liste=liste.split("\n")
fichier.close()
for s in range(1,int(liste[0])+1):
    sortie.write(what_to_write(s,liste[s])+"\n")
sortie.close()


#amelioration : trop de conversions
#(N en liste dont on pourrais soustraire 1 à chaque fois)

##def tidyest_number_v2(N):
##    if len(str(N))==1:
##        return N
##    L=[int(i) for i in str(N)]
##    for k in range(len(str(N))-1):
##        if L[k]>L[k+1]:
##            if L[k]>0:
##
##def is_L_tidy(L):
