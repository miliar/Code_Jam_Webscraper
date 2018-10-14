'''Apr 14, 2012 Autor: Artur'''
# -*- coding: utf-8 -*-
import string

rida = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
rida2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
rida3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv qz"

ridav = "our language is impossible to understand"
rida2v = "there are twenty six factorial possibilities"
rida3v = "so it is okay if you want to just give up zq"

tähed = {}
tähedkatse={}

rida = rida.split(" ")
ridav = ridav.split(" ")
rida2 = rida2.split(" ")
rida2v = rida2v.split(" ")
rida3 = rida3.split(" ")
rida3v = rida3v.split(" ")

for i, sõna in enumerate(rida):
    for j, täht in enumerate(sõna):
        tähed[täht]=ridav[i][j]
        
for i, sõna in enumerate(rida2):
    for j, täht in enumerate(sõna):
        tähed[täht]=rida2v[i][j]
        
for i, sõna in enumerate(rida3):
    for j, täht in enumerate(sõna):
        tähed[täht]=rida3v[i][j] 

vastus=""

file_in = open("A-small-attempt3.in", "r")
file_out = open("A-small-attempt3.out", "w")
for case, rida in enumerate(file_in):
    if case!=0 and rida!="":
        vastus += "Case #" + str(case) + ": "
        for täht in rida:
            if tähed.get(täht)!=None:
                vastus += tähed.get(täht)
            else:
                vastus += " "
        if case!=mitu:
            file_out.write(vastus.strip() + "\n")
        else:
            file_out.write(vastus.strip())
        vastus=""
    else:
        mitu=int(rida)


