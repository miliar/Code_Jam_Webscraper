# -*- coding: utf-8 -*-
import sys

# Le nom du fichier a parser doit être donner en premier argument    
f_in = sys.argv[1]
f_in = open(f_in)

# On récupère le nombre de cas
T = int(f_in.readline())

for i in range(1, T+1):
    L = f_in.readline().split()

    res_l = []
    [A, B] = map(lambda x: int(x), L)

    for j in range(A, B):
        w_j = str(j)
        for k in range(1, len(w_j)):
            r_j = int(w_j[k:]+w_j[:k]) 
            if ((A <= r_j) & (r_j <= B) & (j != r_j)):
                tmp=set([j, r_j])
                if (not tmp in res_l):
                    res_l.append(tmp)

    print "Case #%d: %s" % (i, len(res_l))
