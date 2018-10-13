# -*- coding: utf-8 -*-
import sys
import math

stin = sys.stdin
stin.readline() # 1行読み飛ばし

#"abcdefghijklmnopqrstuvwxyz"
t = "yhesocvxduiglbkrztnwjpfmaq"

tbl = {}
for i,c in enumerate(t):
    tbl[chr(ord('a')+i)] = c

for i,line in enumerate(stin.readlines()):
    def tr(x):
        if x == " " or x=="\n":
            return x
        return tbl[x]

    print "Case #%d: %s" % (i+1, "".join([tr(x) for x in line])),
