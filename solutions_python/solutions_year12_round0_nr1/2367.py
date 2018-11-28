#!/usr/bin/env python

import string
instring = 'abcdefghijklmnopqrstuvwxyz'
outstring = 'yhesocvxduiglbkrztnwjpfmaq'
tab = string.maketrans(string.ascii_lowercase, outstring)
fin = open('1in')
instr = fin.read().strip().split('\n')[1:]
fout = open('1out', 'w')

for index, string in enumerate(instr):
	fout.write("Case #%d: %s\n"%(index + 1, string.translate(tab)))
