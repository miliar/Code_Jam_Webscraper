#! /usr/bin/python -tt

def load_file(chemin):
    from os.path import isfile
    if isfile(chemin):
        fichier = open(chemin, 'r')
        donnees = fichier.readlines()
        fichier.close()

        lignes = []
        for ligne in donnees[1:]:
            ligne = [eval(n) for n in ligne.split()]
            lignes.append((tuple(ligne[:3]),ligne[3:]))
    return lignes

def solve(((N,S,p), googlers)):
    r = [(n+2)/3 for n in googlers]
    if p <= 1:
        up = 0
    else:
        up = googlers.count(3*(p-1)) + googlers.count(3*(p-1)-1)
    return len([1 for n in r if n >= p]) + min(S,up)


from sys import argv

i = 1
for case in load_file(argv[1]):
    print "Case #" + str(i) + ": " + str(solve(case))
    i += 1

