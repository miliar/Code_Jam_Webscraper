"""
For each test case, output one line containing "Case #x: y z",
 where x is the test case number (starting from 1), 
y is the number of points Naomi will score if she plays Deceitful War optimally, 
and z is the number of points Naomi will score if she plays War optimally.
"""
def kenChoose(naomiBlock, ken):
	for block in ken:
		if block > naomiBlock:
			return ken.pop(ken.index(block))
	return ken.pop(0)

infile = open('input.in', 'r')
outfile = open('output.out','w')
numCases = int(infile.readline())
for case in range(numCases):
	numBlocks = int(infile.readline())
	naomi = infile.readline().split()
	ken = infile.readline().split()
	for i in range(numBlocks):
		naomi[i] = float(naomi[i])
		ken[i] = float(ken[i])

	naomi.sort()
	ken.sort()

	warnaomi = list(naomi)
	warken = list(ken)
	#play war
	war = 0
	for i in range(numBlocks):
		naomiChosen = warnaomi.pop()
		if kenChoose(naomiChosen,warken) < naomiChosen:
			war +=1

	#play deceitful war
	def loseCond():
		for i in range(len(ken)):
			if ken[i] > naomi[i]:
				return True
		return False
	lose = loseCond()
	while lose:
		naomiChosen = naomi.pop(0)
		naomiTold = ken[-1]-0.000001
		kenChoose(naomiTold,ken)
		lose=loseCond()
	deceitful = len(naomi)



	outfile.write("Case #{x}: {y} {z}\n".format(x=case+1, y=deceitful, z=war))

infile.close()
outfile.close()
