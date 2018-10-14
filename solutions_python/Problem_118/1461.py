#!/usr/bin/python

import re
import sys
from math import sqrt 
zbior={}

if len(sys.argv)>1 :
    plik=open(sys.argv[1])
    dane=plik.readlines()
else:
    dane=sys.stdin.readlines()

liczba=int(dane[0].strip())

class GetOutOfLoop(Exception):
    pass


sprawa=0

for x in dane[1:]:
    (poczatek,koniec)=x.strip().split()
    licznik=0
    sprawa=sprawa+1
    for a in xrange(int(poczatek),int(koniec)+1):
        try:
            if str(a)==str(a)[::-1]:
                try:
                    if zbior[a]==1:
                        raise GetOutOfLoop
                except KeyError:
                    pass
                pierwiastek=sqrt(a)
                if pierwiastek==int(pierwiastek) and str(int(pierwiastek))==str(int(pierwiastek))[::-1]:
                    raise GetOutOfLoop
        except GetOutOfLoop:
            licznik=licznik+1
            zbior[a]=1

    print "Case #%d: %d" %(sprawa,licznik) 

            
            


#    print "Case #%d: %s" % (licznik, funkcja(tablica))



        

