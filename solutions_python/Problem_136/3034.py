r = open("./input.txt", "r")
w = open("./output.txt", "w")

numCases = r.readline()

for c in range(1, int(numCases)+1):
	test = map(float, r.readline().split())
	farmCost = test[0]
	farmBonus = test[1]
	goal = test[2]
	numFarms = 0.0
	time = 0.0
	while (goal/(2.0+numFarms*farmBonus)) > (farmCost/(2.0+numFarms*farmBonus)+goal/(2.0+(numFarms+1)*farmBonus)):
		time += farmCost/(2+numFarms*farmBonus)
		numFarms += 1.0
	time += (goal/(2.0+numFarms*farmBonus))
	w.write("Case #"+str(c)+": "+str(time)+"\n")

r.close()
w.close()