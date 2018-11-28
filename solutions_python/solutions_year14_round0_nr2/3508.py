

if __name__ == "__main__":
	N = int(raw_input())
	
	for case in range(1,N+1):
		line = raw_input()
		C, F, X = [ float(u) for u in line.split() ]
		sol = X / 2
		numFarm = 1
		while True:
			val = sum(map(lambda x : C / (2+F*x), range(0, numFarm))) + X / (2 + F * numFarm)
			if val > sol:
				break
			sol = val
			numFarm = numFarm + 1
		print "Case #" + str(case) + ": %.07f" % round(sol, 7)
