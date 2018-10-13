fil = file("output.txt", "w")
fil1 = file("input.txt", "r")
testcases = int(fil1.readline())
for i in range(testcases):
	sMax,shyness = fil1.readline().split(' ')
	sMax = int(sMax)
	shyness = shyness.strip()
	standing = 0
	extra = 0
	for j in range(len(shyness)):
		if(j<=standing or int(shyness[j]) == 0):
			standing += int(shyness[j])
		else:
			ekstra = j-standing
			extra += ekstra
			standing += int(shyness[j]) + extra
	fil.write("Case #"+ str(i+1) + ": " + str(extra))
	fil.write("\n")
fil1.close()
fil.close()