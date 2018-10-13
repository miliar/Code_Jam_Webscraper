# -*- coding: utf-8 -*-
import sys

getline=sys.stdin.readline;

T=int(getline());
print >> sys.stderr, 'T={0}'.format(T)

for idx in range(T):
    print >> sys.stderr, '========================================'

    # récupération des variables
    V=getline().split(" ");
    N=int(V[0]);
    K=int(V[1]);

    # affichage des variables
    print >> sys.stderr, ' N={0}'.format(N);   # nombre de snappers
    print >> sys.stderr, ' K={0}'.format(K);   # nombre de claquement de doigts

    # recherche et affichage de la solution
    print 'Case #{0}:'.format(idx+1),
    if (K-((2**N)-1))%(2**N):
        print 'OFF';
    else:
        print 'ON';

