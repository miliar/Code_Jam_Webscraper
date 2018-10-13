#!/usr/bin/python

import re
import sys



if len(sys.argv)>1 :
    plik=open(sys.argv[1])
    dane=plik.readlines()
else:
    dane=sys.stdin.readlines()

def funkcja(tab):
    for x in range(0,len(tab)):
        tab[x]=tab[x].strip().split(" ")
        tab[x]=map(lambda a: int(a),tab[x])
    ziptab=zip(*tab)
    class GetOutOfLoop( Exception ):
        pass
    try: 
        for x in range(0,len(tab)):
            for y in range(0,len(tab[x])):
                poziome=len(filter(lambda a: a>tab[x][y],tab[x]))
                pionowe=len(filter(lambda a: a>tab[x][y],ziptab[y]))
                if (pionowe > 0 and poziome > 0):
                    raise GetOutOfLoop
        OK="YES"
    except GetOutOfLoop:
        OK="NO"
    return OK

liczba=int(dane[0].strip())

wymiary=dane[1].strip().split(" ")
wymiary[0]=int(wymiary[0])
wymiary[1]=int(wymiary[1])
wskaznik=2
dzialac=True
licznik=1
while dzialac:
    tablica=dane[(wskaznik):(wskaznik+wymiary[0])]
    print "Case #%d: %s" % (licznik, funkcja(tablica))
    licznik=licznik+1
    wskaznik=wskaznik+wymiary[0]+1
    liczba-=1
    if liczba>0:
        wymiary=dane[wskaznik-1].strip().split(" ")
        wymiary[0]=int(wymiary[0])
        wymiary[1]=int(wymiary[1])
    else:
        dzialac=False



        

