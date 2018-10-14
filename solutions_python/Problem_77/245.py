#!/usr/python
#encoding=utf-8

import sys

try :
    fichier = open(sys.argv[1], "r")
except:
    print "problème lors de l'ouverture du fichier"

lignes  = fichier.readlines()


nb_case = lignes[0].strip("\n")
lignes.pop(0)

# nettoie la liste des lignes
for i,l in enumerate(lignes):
    lignes[i] = l.strip("\n")
    
compteur = 1
for k, ligne in enumerate(lignes):

    if k%2:
        array = ligne.split()
        # print array
        bonne_place = []
        for k, n in enumerate(array):
            if int(n) == int(k+1) :
                bonne_place.append(n)
                
        # print "à la bonne place ", bonne_place
        
        verouille = []
        verouille.extend(bonne_place)
        
        # print "verouille: ", verouille
        
        nb_libres = len(array)-len(verouille)
        # print nb_libres, " libres, donc 1/" , nb_libres, " de chance"
        
        print "Case #%d: %f" % (compteur, nb_libres)
        compteur = compteur +1
        
        
        # print "\n"
        
        
try :
    fichier.close()
except: 
    print "problème lors de la fermeture du fichier"