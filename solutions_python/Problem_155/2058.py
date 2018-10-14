f = open("A-large.in")
w = open("Result_A-large.txt","w")

numOfProb = f.readline()

for i in range(int(numOfProb)):
	line = f.readline().split()
	friends = 0
	standing = 0
	for j in range(int(line[0])+1):
		people = int(line[1][j])
		if standing<j:
			friends+=j-standing
			standing+=j-standing
		standing+=people
	w.write("Case #"+str(i+1)+": "+str(friends)+"\n")

f.close()
w.close()
