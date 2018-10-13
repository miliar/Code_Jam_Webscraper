	

f = open("a.in", "r")
data = f.read().split("\n")[1:]
f.close()
if data[-1] == "": data = data[:-1]
data = [d.split(" ")[1] for d in data]

fout = open("a.out", "w")

for i in xrange(len(data)):
	c = 0
	s = 0
	for needed in xrange(len(data[i])):
		howManyToSumIfEnough = int(data[i][needed])
		if needed <= c:
			c += howManyToSumIfEnough
		else:
			s += needed - c
			c += howManyToSumIfEnough + needed - c
		#print howManyToSumIfEnough, "need", needed, "people.", "standed up then (added):",  howManyToSumIfEnough, "with total of", c
	
	S = "Case #%d: %d" % (i+1, s)
	print S
	fout.write(S+"\n")
