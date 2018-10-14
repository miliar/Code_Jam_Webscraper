import os, sys
import re

plik1 = open("dane.txt", "r")
linia1 = plik1.readline().strip().split(' ')
l = int(linia1[0])
d = int(linia1[1])
n = int(linia1[2])

dane = []
i = 1

for linia in plik1.readlines():
  dane.append(linia)

plik1.close()

slownik = ' '.join(dane[:d]).strip()
pytania = dane [d:d+n]

plik2 = open("wynik.txt", "w")
linia = 1

for pytanie in pytania:
  p = re.compile(pytanie.strip().replace('(','[').replace(')',']'))
  plik2.write("Case #%d: %d\n"%(linia, len(p.findall(slownik))))
  linia = linia + 1

plik2.close()
