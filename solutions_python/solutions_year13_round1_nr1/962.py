import math
f = open("in.txt")
T = int(f.readline())

w = open("out.txt", "w")

for i in range(T):
	line = f.readline().split()
	r = long(line[0])
	t = long(line[1])
	counter = 0
	nextcost = (r+1)**2 - r**2
	while nextcost <= t:
		t -= nextcost
		counter += 1
		nextcost = (2*counter + r + 1)**2 - (2*counter + r)**2
	w.write("Case #" + str(i+1) + ": " + str(counter) + "\n")