from sys import argv

script, rname, wname = argv

casefile = open(rname)
outfile = open(wname, 'w')

tc = int(casefile.readline())

coded = "abcdefghijklmnopqrstuvwxyz"
origl = "YHESOCVXDUIGLBKRZTNWJPFMAQ"

for i in range(0,tc):
	text = casefile.readline()

	for l in range(0,26):
		text = text.replace(coded[l],origl[l])
	
	print("Case #%d: %s" % (i+1, text.lower()))
	outfile.write("Case #%d: %s" % (i+1, text.lower()))

casefile.close()
outfile.close()