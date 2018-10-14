lines = open("/home/vic/Downloads/A-large.in").readlines()[1:]
outfile = open("pan", "a+")

for lineNum, a in enumerate(lines):
	flipper = int(a.split()[1])
	pancakes = a.split()[0]

	pairs = [i for i in pancakes]
	i = 0

	flips = 0
	while (i < len(pairs)):
		if pairs[i] == '-' and (i + flipper) <= len(pairs):
			flips += 1
			for f in xrange(i, i+flipper):
				if pairs[f] == "+":
					pairs[f] = "-"
				else:
					pairs[f] = "+"

		i += 1
	
	if '-' in pairs:
		outfile.write("Case #%d: IMPOSSIBLE\n"%(lineNum+1))
		continue
	outfile.write("Case #%d: %d\n"%(lineNum+1, flips))
