from string import maketrans
infile = raw_input("File: ")
contents = open(infile, 'r')
output = open(infile[:-3]+"_solution"+infile[-3:], "w")

translation = {'z':'q', 'q':'z'}
counter = 1

googlerese = """ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv""".split()
english = """our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up""".split()

for goog, eng in zip(googlerese, english):
	for g, e in zip(goog, eng):
		translation[g] = e

for line in contents:
	try:
		int(line)
	except:
		output.write("Case #"+str(counter)+": "+line.translate(maketrans(''.join(translation.keys()), ''.join(translation.values()))))
		#print("Case #"+str(counter)+": "+line.translate(maketrans(''.join(translation.keys()), ''.join(translation.values()))))
		counter += 1
