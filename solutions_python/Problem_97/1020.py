#! /usr/bin/python -tt

def load_file(chemin):
    from os.path import isfile
    if isfile(chemin):
        fichier = open(chemin, 'r')
        donnees = fichier.readlines()
        fichier.close()

    return [(eval(a), eval(b)) for [a,b] in [ligne.split() for ligne in donnees[1:]]]

def solve((a, b)):
    def recycled(n, m):
        n = str(n)
        m = str(m)
        nn = n[1:] + n[0]
        while nn != n:
            if nn == m:
                return 1
            nn = nn[1:] + nn[0]
        return 0
    i = 0
    for n in range(a, b):
        for m in range(n,b+1):
            if recycled(n, m):
                i += 1
    return i

from sys import argv

i = 1
for case in load_file(argv[1]):
    print "Case #" + str(i) + ": " + str(solve(case))
    i += 1

