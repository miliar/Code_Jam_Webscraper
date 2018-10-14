content = open("D-large.in", "r").read().split("\n")
output = open("warout.txt", "w")
inputsize = int(content[0])
print len(content)
for i in range(1, inputsize+1):
	naomipointsdwar = 0
	naomipointswar = 0
	Naomi = content[i*3-1].split(" ")
	BenK = content[i*3].split(" ")
	BenJ = content[i*3].split(" ")
	for j in range(0, len(Naomi)):
		Naomi[j] = float(Naomi[j])
		BenK[j] = float(BenK[j])
		BenJ[j] = float(BenJ[j])
	BenK = sorted(BenK)
	BenJ = sorted(BenJ)
	for item in sorted(Naomi):
		k = 0
		j = 0
		iitem = BenK[len(BenK)-1]-0.000001
		while(k < len(BenK)-1 and iitem > BenK[k] and item < BenK[k]):
			k += 1
		while(j < len(BenJ)-1 and item > BenJ[j]):
			j += 1
		if BenK[k] < item:
			naomipointsdwar += 1
		if BenJ[j] < item:
			naomipointswar += 1
		BenK.remove(BenK[k])
		BenJ.remove(BenJ[j])
		Naomi.remove(item)
	output.write("Case #{0}: {1} {2}\n".format(i,naomipointsdwar, naomipointswar))				
