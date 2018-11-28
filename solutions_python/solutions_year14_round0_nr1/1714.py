filename1 = "A-small-attempt0.in.txt"
filename2 = "Output.txt"

with open(filename2,'w') as g:
	with open(filename1,'r') as f:
		T = int(f.readline())
		for i in range(1,T+1):
			R1 = int(f.readline())
			for j in range(1,5):
				temp = f.readline().split()
				if j == R1:
					check1 = temp
			R2 = int(f.readline())
			for j in range(1,5):
				temp = f.readline().split()
				if j == R2:
					check2 = temp
			ans = []
			for x in check1:
				if x in check2:
					ans.append(x)
			if len(ans) == 1:
				g.write("Case #%s: %s\n" % (i, ans[0]))
			elif len(ans) == 0:
				g.write("Case #%s: Volunteer cheated!\n" % (i))
			else:
				g.write("Case #%s: Bad magician!\n" % (i))