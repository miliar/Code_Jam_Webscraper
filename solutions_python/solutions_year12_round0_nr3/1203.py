def test(m, n):
	for i in range(len(m)):
		if((m[i:] + m[0:i]).lstrip('0') == n.lstrip('0')):
			return True
	return False
	
def runCase(A, B):
	tot = 0
	for n in range(A, B):
		for m in range(n+1, B+1):
			#print(str(n) + " : " + str(m))
			if test(str(m), str(n)):
				tot = tot + 1
	return tot


#runCase(10, 20)

counter = 0
output = open('outputC.txt', 'w')
with open('inputC.txt', 'r') as f:
	for fileLine in f:
		fileLine = fileLine.split()
		if (counter == 0):
			counter = counter + 1
			continue
		
		output.write("Case #" + str(counter) + ": " + str(runCase(int(fileLine[0]), int(fileLine[1]))) + "\n")
		counter = counter + 1

output.close()
f.close()
