inputFile = raw_input("Input file: ")
with open(inputFile) as f:
	content = f.readlines()
f.close()

def getFirst(stuff):
	return stuff.pop(0)

n = int(getFirst(content))
output = ""
BASERATE = 2.0

for i in range(n):
	params = getFirst(content).split()
	c, f, x = float(params[0]), float(params[1]), float(params[2])

	times = [x/BASERATE]

	currentTime = 0.
	totalFarms = 0.

	while len(times) == 1 or (currentTime + x/(BASERATE + totalFarms*f)) <= times[-2]:
		currentTime += c/(BASERATE + totalFarms*f)
		totalFarms += 1.
		times.append(currentTime + x/(BASERATE + totalFarms*f))
		#print (currentTime + x/(BASERATE + totalFarms*f)), times[-2]
	output += "Case #" + `i + 1` + ": " + `min(times)` + "\n"

f = open("cookieClickerOutput.txt", "w")
f.write(output)
f.close()