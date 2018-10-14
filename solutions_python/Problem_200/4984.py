def tiny(chaine):
    resultat=False
    if len(chaine)>1:
        for i in range(1,len(chaine)):
            if int(chaine[i-1])>int(chaine[i]):
                resultat=True
    return resultat

def trouverNombre(nombre):
    nonTiny=True
    while nonTiny:
        nombreString=str(nombre)
        nonTiny=tiny(nombreString)
        if nonTiny:
            nombre-=1
    return nombre

nom="B-small-attempt1.in"
fichier=open(nom,"r")
taille=fichier.readline()
contenu=[]
for i in range(int(taille)):
    ligne=fichier.readline()
    ligne=ligne[:-1]
    contenu+=[ligne]
fichier.close()
sortie=open("resultat.txt","w")
for test in range(len(contenu)):
    resultat=trouverNombre(int(contenu[test]))
    sortie.write("Case #"+str(test+1)+": "+str(resultat)+"\n")
sortie.close()
