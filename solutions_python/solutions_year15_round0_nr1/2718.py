with open("A-large.in", 'r') as rf:
	with open("output.txt", 'w') as wf:
		for i in range(int(rf.readline())):
			tok = rf.readline().split(" ")
			mx = int(tok[0])
			dz = tok[1]
			
			out = 0
			tot = 0
			for j in range(0, mx+1):
				dg = int(dz[j])
				if (j > tot):
					st = j - tot
					out += st
					tot += st + dg
				else:
					tot += dg
				
			wf.write("Case #" + str(i+1) + ": " + str(out) + "\n")