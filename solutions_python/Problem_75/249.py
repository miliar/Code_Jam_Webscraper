#!/usr/python
#encoding=utf-8

import sys 

def findResult(e_base, a, b):

    for e in e_base:
        if (e[0] == a and e[1] == b) or (e[0] == b and e[1] == a):

            return e[2]
    return None
    
def opposition(oppositions, list):
    a = list[-1]
    for o in oppositions :
        # si le nouvel element est dans la liste des elem opposables
        if o[0] == a or o[1] == a :
            if o[0] == a :
                
                # opposition !
                if o[1] in list :
                    # print "opposition"
                    list[:] = []
                    return
                    
            else:
                
                # opposition !
                if o[0] in list :
                    # print "opposition"
                    list[:] = []
                    return
                
            

try :
    fichier = open(sys.argv[1], "r")
except:
    print "problème lors de l'ouverture du fichier"


lignes  = fichier.readlines()

base    = ("Q", "W", "E", "R", "A", "S", "D", "F")

nb_case = lignes[0].strip("\n")
lignes.pop(0)

# nettoie la liste des lignes
for k,l in enumerate(lignes):
    lignes[k] = l.strip("\n")



for k, ligne in enumerate(lignes):
    ligne = ligne.split()
    
    e_base  = ligne[1:int(ligne[0])+1]
    ligne   = ligne[int(ligne[0])+1:]
    # print e_base
    
    oppositions = ligne[1:int(ligne[0])+1]
    ligne       = ligne[int(ligne[0])+1:]
    
    
    to_invoke = ligne[1:][0]
    
    resultat    = []
    
    for elem in to_invoke:
        # print "--%s--" % elem
        
        if len(resultat) < 1 :
            resultat.append(elem)
            
        else :
            if (resultat[-1] in base) and (elem in base):
                donne = findResult(e_base, resultat[-1], elem)
                if donne :
                    # print "trouvé, %s et %s donne un %s" % (resultat[-1], elem, donne)
                    resultat[-1:] = donne
                else :
                    resultat.append(elem)
                    
            # aucune combinaison
            else :
                resultat.append(elem)
            
            opposition(oppositions, resultat)
        # print resultat
    
    print "Case #%d: [%s]" %(k+1, ", ".join(resultat))
    # print "result:\t\t", resultat
    # print "e_base:\t\t", e_base
    # print "opposition:\t", oppositions
    # print "to invoke:\t", to_invoke
    # 
    # 
    # print "---------------------"

try :
    fichier.close()
except: 
    print "problème lors de la fermeture du fichier"