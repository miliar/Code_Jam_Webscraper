#!/usr/bin/python

from string import maketrans

translator = maketrans("abcdefghijklmnopqrstuvwxyz", "yhesocvxduiglbkrztnwjpfmaq")

f = open('input.in', 'rb')
t = int(f.readline())
input_data = f.readlines()
f.close()

case = 1
f = open('output.out', 'wb')
for line in input_data:
	f.write("Case #%d: %s" % (case,line.translate(translator)))
	case += 1
f.close()

print "Done."
