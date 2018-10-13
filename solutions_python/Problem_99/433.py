filein = open('./A-small-attempt0.in', 'r')
fileout = open('./A-small-attempt0.out', 'w')
lines = filein.readlines()

data = {}
for i, line in enumerate(lines):
	if not i == 0:
		if i % 2 == 1:
			data[(i+1)/2] = {}
			temp = line.split(' ')
			a = int(temp[0])
			b = int(temp[1])
			data[(i+1)/2]["A"] = a
			data[(i+1)/2]["B"] = b
		elif i % 2 == 0:
			data[(i+1)/2]["list"] = []
			temp = line.split(' ')
			for j in temp:
				data[(i+1)/2]["list"].append(float(j))

exp = []
for i in data:
	a = data[i]["A"]
	b = data[i]["B"]
	temp = 2 + b
	for n, j in enumerate(data[i]["list"]):
		prob = 1
		for k in range(0, a - n):
			prob *= data[i]["list"][k];
		tempE = (2*n + 2*b - a + 2)*(1-prob) + (2*n + b - a + 1)*(prob)
		if (tempE < temp):
			temp = tempE
	exp.append(temp)


for e, val in enumerate(exp):
	fileout.write("Case #" + str(e+1) + ": " + str(val) + "\n")

filein.close()
fileout.close()