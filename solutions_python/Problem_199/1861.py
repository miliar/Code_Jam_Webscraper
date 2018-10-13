
infile = open("A-large.in", "r")
lines = infile.readlines()
outfile = open("out.out", "w")
tc = int(lines[0])



for t in range(tc):
	(pc, s) = lines[t+1].strip().split(" ")
	s = int(s)
	
	f = 0
	p = 1
	i = 0	
	for i in range(len(pc)):
		#print("ok", pc)
		if pc[i] == '-':
			if i+s-1 < len(pc):
				#print("hi")
				f += 1
				for j in range(s):
					if pc[i+j] == '+':
						pc = pc[0:i+j] + '-' + pc[i+j+1:]
					else:
						pc = pc[0:i+j] + '+' + pc[i+j+1:]
			else:
				p = 0
				#print("lol")
				break

	if p == 1:
		outfile.write("Case #" + str(t+1) + ": " + str(f) + "\n")
	else:
		outfile.write("Case #" + str(t+1) + ": IMPOSSIBLE\n")