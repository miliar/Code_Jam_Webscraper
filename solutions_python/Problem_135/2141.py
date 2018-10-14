def solve(a, b, am, bm):
	row1 = am[a-1]; row2 = bm[b-1]
	ans = []
	for r1 in row1:
		if r1 in row2:
			ans.append(r1)
	if len(ans) == 1:
		return str(ans[0])
	elif len(ans) == 0:
		return "Volunteer cheated!"
	elif len(ans) > 1:
		return "Bad magician!"
	raise NotImplementedError

if __name__ == "__main__":
	import sys
	f = open(sys.argv[1], "r")
	T = int(f.readline())
	for case in range(1, T+1):
		a= int(f.readline())
		am = []
		for i in range(4):
			am.append(map(int, f.readline().split()))
		b= int(f.readline())
		bm = []
		for i in range(4):
			bm.append(map(int, f.readline().split()))
		print "Case #"+str(case)+": "+solve(a, b, am, bm)
