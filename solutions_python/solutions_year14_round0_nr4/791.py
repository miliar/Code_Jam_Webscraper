import sys

def main(argv):
	with open(argv) as inputFile:
		testcases = inputFile.readline()

		for t in range (0, int(testcases)):
			# print "Test case: "+str(t+1)

			blocks = int(inputFile.readline())
			naomi = inputFile.readline().split()
			ken = inputFile.readline().split()

			naomi.sort(reverse=True)
			ken.sort(reverse=True)

			y = dwar(blocks, naomi, ken)
			z = war(blocks, naomi, ken)

			# print "Case #"+str(t+1)+": "+y+" "+z
			with open('output.txt', 'a') as output:
				output.write("Case #"+str(t+1)+": "+y+" "+z+"\n")

def dwar(blocks, naomi, ken):
	xnaomi = list(naomi)
	xken = list(ken)

	dwar_win = 0
	for n in xnaomi:
		for k in xken:
			if n > k:
				dwar_win+=1
				xken.remove(k)
				break

	# print "dwar win: "+str(dwar_win)
	return str(dwar_win)

def war(blocks, naomi, ken):
	xnaomi = list(naomi)
	xken = list(ken)

	war_win = blocks
	for k in xken:
		for n in xnaomi:
			if k > n: 
				war_win-=1
				xnaomi.remove(n)
				break

	# print "war win: "+str(war_win)
	return str(war_win)

if __name__ == "__main__":
	# main(sys.argv[1:])
	main("D-large.in")