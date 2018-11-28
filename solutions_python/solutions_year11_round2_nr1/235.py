#! /usr/bin/env python3.0

def makeRow(string):
    
    retour = []
    
    for r in string:
        if ((r == "1") or (r == "0")):
            retour.append(int(r))
        else:
            retour.append(None)
    return retour

def nbO(liste):
    tot = 0
    for i in liste:
        if (not i == None):
            tot+=1
    return tot

def rpi(tab, indice):
    # print("WP", wp(tab[indice]))
    # print("OWP", owp(tab,indice))
    # print("OOWP", oowp(tab,indice))
    return 0.25 * wp(tab[indice]) + 0.5 * owp(tab, indice) + 0.25 * oowp(tab, indice)

def wp(liste, indice_moins=-1):
    total = 0
    won = 0
    for i,e in enumerate(liste):
        if (i == indice_moins):
            continue
        if (not e == None):
            total += 1
            won += e
    return won/total

def owp(tab, indice):
    
    somme = 0
    total = nbO(tab[indice])
    
    for i,e in enumerate(tab):
        if (i == indice):
            continue
        if (not tab[indice][i] == None): 
            somme += wp(e, indice)
    
    return somme/total

def oowp(tab, indice):
    
    somme = 0
    
    total = nbO(tab[indice])
    
    for i,e in enumerate(tab):
        if (i == indice):
            continue
        if (not tab[indice][i] == None): 
            somme += owp(tab, i)
    
    return somme/total

fic = input()

f = open(fic, "r")

lines = [li.replace("\n", "") for li in f.readlines()]

T = int(lines[0])

lines = lines[1:]

f.close()

f = open("output.txt", "w")

curseur = 0

for i in range(T):
    
    tab = []
    
    for j in range(1, int(lines[curseur])+1):
        tab.append(makeRow(lines[curseur+j]))
    
    curseur += int(lines[curseur])+1
    
    # tab: [[...], [...], [...]]
    
    out = "Case #"+str(i+1)+":\n"
    
    for i in range(len(tab)):
        out += str(rpi(tab, i))
        
        if (not i == len(tab)-1):
            out += "\n"
    
    print(out)
    f.write(out+"\n")

f.close()