#!/usr/bin/python

from string import maketrans

al = "abcdefghijklmnopqrstuvwxyz"
ou = "yhesocvxduiglbkrztnwjpfmaq"
# ou = "ynficwlbkuomxsevzpdrjgthaq"
tr = maketrans(al, ou)

T = input()
for x in range(T) :
    str =  raw_input();
    print "Case #%d: " %(x + 1) + str.translate(tr);
