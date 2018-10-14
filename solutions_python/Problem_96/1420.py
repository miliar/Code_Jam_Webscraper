myfile = open("2.in", 'r')
f = myfile.readlines()
outfile = open('2.out', 'w')

count = 1
for line in f:
	lineArray = [int(x) for x in line.strip().split()]
	if len(lineArray) < 3:
		continue
	N = lineArray.pop(0)
	S = lineArray.pop(0)
	p = lineArray.pop(0)

	#LineArray now only contains total points

	#Hard coding in maximum possibles
	NonspecP = (p*3) -2
	SpecP = (p*3)-4
	#Exceptions if p = 1
	if p == 1:
		SpecP = 1

	Over = 0
	for i in sorted(lineArray):
		if i >= NonspecP:
			Over += 1
		elif i >= SpecP and S > 0:
			Over += 1
			S -= 1

	outfile.write("Case #%d: %d\n" %(count, Over))
	count += 1
