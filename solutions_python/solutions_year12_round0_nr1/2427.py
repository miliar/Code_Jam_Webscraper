import fileinput
import string

table = string.maketrans('abcdefghijklmnopqrstuvwxyz', 'yhesocvxduiglbkrztnwjpfmaq')

def translate(s):
	return string.translate(s, table)

limit = -1

for i, line in enumerate(fileinput.input()):
	if i == 0:
		limit = int(line)
		continue
	
	if limit != -1 and i > limit:
		continue
	print "Case #"+str(i)+":",translate(line),
