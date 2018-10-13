import sys

f = open(sys.argv[1])
out = open(sys.argv[1].replace("in","out"), "w")
cnt = int(f.readline().strip("\n"))
for i in range(cnt):
	input = f.readline().strip("\n").split(" ")[1:]
	pairs = []
	
	for j in range(0,len(input),2):
		pairs.append((input[j], int(input[j+1])))
	
	steps = 0
	Osteps = 0
	Opos = 1
	Bsteps = 0	
	Bpos = 1
	for p in pairs:
		if p[0] == "O":
			cost = max(abs(Opos - p[1]) - Osteps + 1, 1)
			Opos = p[1]
			Osteps = 0
			Bsteps += cost
			steps += cost
		else:
			cost = max(abs(Bpos - p[1]) - Bsteps + 1, 1)
			Bpos = p[1]
			Bsteps = 0
			Osteps += cost
			steps += cost
	out.write("Case #%s: %s\n" % (i + 1, steps))
	
	