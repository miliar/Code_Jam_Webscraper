from string import ascii_lowercase, maketrans

case = 1
# worked out by hand ;)
table = maketrans (ascii_lowercase, 'yhesocvxduiglbkrztnwjpfmaq')

with open('small.txt') as f:
	lines = f.readlines()[1:]
	for line in lines:
		print "Case #%d: %s" % (case, line.strip().translate (table))
		case += 1