# -*- coding: utf-8 -*-
import sys

def intersect(a, b):
    if ( (a[0]>b[0]) and (a[1]<b[1]) ) or ( (a[0]<b[0]) and (a[1]>b[1]) ):
        return 1
    return 0

getline=sys.stdin.readline;

T=int(getline());
print >> sys.stderr, 'T={0}'.format(T)

for idx in range(T):
    print >> sys.stderr, '========================================'

    # récupération des variables
    N=int(getline());
    L=[];
    for i in range(N):
        J=getline().split(" ");
        L.append((int(J[0]), int(J[1])));

    # affichage des variables
    print >> sys.stderr, ' N={0}'.format(N);   # nombre de fils
    print >> sys.stderr, ' L={0}'.format(L);   # liste des positions des fils

    # recherche et affichage de la solution
    print 'Case #{0}:'.format(idx+1),
    nb=0;
    for s in range(N-1):
        for i in range(s+1, N):
#            print "(%d, %d)" % (s, i),
            if intersect(L[s], L[i]):
                nb=nb+1
    print nb


