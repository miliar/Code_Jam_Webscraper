def freecell(n,d,g):
	minN = [0 for i in range(101)]
	if g == 0 and d != 0:
		return "Broken"
	if g == 100 and d != 100:
		return "Broken"
	for i in [1,2,4,5,10,20,25,50,100]:
		for j in range(i+1):
			if minN[100*j/i] == 0:
				minN[100*j/i] = i
	if minN[d] <= n and minN[d] != 0:
		return "Possible"
	return "Broken"
	
def solveFreecell():
	f = open('gcjdata.txt','r')
	lines = f.readlines()
	for i in range(1,len(lines)):
		data = lines[i].split(" ")
		print "Case #{0}: {1}".format(i,freecell(int(data[0]),int(data[1]), int(data[2])))
		
solveFreecell()