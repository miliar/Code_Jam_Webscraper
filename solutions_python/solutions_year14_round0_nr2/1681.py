filename1 = "B-small-attempt0.in.txt"
filename2 = "Output.txt"

with open(filename2,'w') as g:
	with open(filename1,'r') as f:
		T = int(f.readline())
		for i in range(1,T + 1):
			temp = f.readline().split()
			C = float(temp[0])
			F = float(temp[1])
			X = float(temp[2])
			baseold = X + 1
			basenew = X
			bought = 0
			while basenew < baseold:
				Timer = X / (2 + F * bought)
				for x in range(bought):
					Timer += C / (2 + F * x)
				baseold = basenew
				basenew = Timer
				bought += 1
			g.write("Case #%s: %s\n" % (i,"%.7f" % baseold))
		