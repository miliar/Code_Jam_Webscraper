#!/usr/bin/env python

import sys

mapping = "yhesocvxduiglbkrztnwjpfmaq"

t = int(raw_input())
for i in range(t):
    line = raw_input()
    line2 = ""
    for char in line.strip():
        if char==' ':
            line2 += " "
        else:
            line2 += mapping[ord(char.lower())-ord('a')]
    print "Case #%d: %s" % (i+1,line2)

