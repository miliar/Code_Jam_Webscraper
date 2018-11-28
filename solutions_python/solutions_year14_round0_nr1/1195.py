# Input data
infile = "A-small-attempt0.in"
with open(infile, 'r') as f:
	data = f.read().split("\n")
	
# Cases
bad = "Bad magician!"
cheat = "Volunteer cheated!"
	
testCases = int(data[0])
dataL = data.__len__()

# Each case solution
c = 1
results = []
while c < dataL:
	# First question
	rowChoose = int(data[c])
	rowChoose1 = data[c+rowChoose].split(" ")
	c += 5
	# Second question
	rowChoose = int(data[c])
	rowChoose2 = data[c+rowChoose].split(" ")
	c += 5
	# Checking
	auxResult = []
	for i in rowChoose1:
		if i in rowChoose2:
			auxResult.append(i)
	# Result case
	if auxResult.__len__() == 0:
		results.append(cheat)
	elif auxResult.__len__() == 1:
		results.append(auxResult[0])
	else:
		results.append(bad)
		
#Output data
outfile = "out.txt"
with open(outfile, 'w') as f:
	for i in range(testCases):
		f.write("Case #%i: %s\n" % (i+1, results[i]))
