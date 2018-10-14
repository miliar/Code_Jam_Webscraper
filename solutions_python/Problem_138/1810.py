f=open("D-small-attempt0.in", "r")
listeResultsWar=[]
listeResultsdeceitfulWar=[]
naomiWood=[]
kenWood=[]
nbTest = int(f.readline())
i=0

def parcoursGrand(naomi):
    plusgrand=0.0
    for k in range(len(naomi)):
        if float(naomi[k])>float(plusgrand):
            plusgrand=naomi[k]
    return plusgrand

def deceitfulWar(naomi,ken):
    print(ken)
    nbWin=0
    for z in range(len(naomi)):
        
        plusgrandKen=0.0
        plusgrand=parcoursGrand(naomi)

        for zz in range(len(ken)):
            if float(ken[zz])<float(plusgrand) and float(ken[zz])>float(plusgrandKen):
                plusgrandKen=ken[zz]
        if float(plusgrand)>float(plusgrandKen):
            nbWin+=1
        naomi.remove(plusgrand)
        print(plusgrandKen)
        if plusgrandKen!= 0.0:

            ken.remove(plusgrandKen)
        else:

            return(nbWin-1)
    return nbWin
        
        
def war(naomi,ken):
    nbWin=0
    copieK=ken
    for z in range(len(naomi)):
        pluspetit=2000.0
        for zz in range(len(copieK)):
            if (float(copieK[zz])<float(pluspetit)) and (float(copieK[zz])>float(naomi[z])):
                pluspetit=copieK[zz]
        if pluspetit==2000.0:
            for zzz in range(len(copieK)):
                if float(copieK[zzz])<float(pluspetit):
                    pluspetit=copieK[zzz]
            nbWin+=1
        copieK.remove(pluspetit)
    return(nbWin)

for ligne in f:
    if i==1:
        naomiWood=ligne.rstrip('\n\r').split(" ")
    if i==2:
        kenWood=ligne.rstrip('\n\r').split(" ")
        copieK=ligne.rstrip('\n\r').split(" ")
    i+=1
    if i==3:

        listeResultsWar.append(war(naomiWood,kenWood))

        listeResultsdeceitfulWar.append(deceitfulWar(naomiWood,copieK))
        
        i=0
print(listeResultsWar)
print(listeResultsdeceitfulWar)

f.close()
f=open("Output.txt", "w")
z=0
while z < nbTest:

    f.write("Case #"+ str(z+1)+": "+str(listeResultsdeceitfulWar[z])+" "+str(listeResultsWar[z])+'\n')

    z+=1
f.close()
