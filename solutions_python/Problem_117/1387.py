def lawn(myfile):
	f = open(myfile, "r")
	g = open("file6.out", "w")
	numExamples = int(float(f.readline()))
	k = 1
	while (k < numExamples+1):
		N,M = f.readline().split()
		N = int(float(N))
		M = int(float(M))
		lines = []
		columns = []
		for i in range(0,N):
			lines.append([int(float(i)) for i in f.readline().split()])
		for i in range(0,M):
			column = []
			for j in range(0,N):
				p = int(float(lines[j][i]))
				column.append(p)
			columns.append(column)
		print(lines)
		print(columns)
		
		for n in range(0,N): #for each row
			for m in range(0,M): #for each col in row
				case = ""
				found = False
				pixel = lines[n][m]
				# check if all numbers in same row are lower or equal
				for t in range(0,M):
					neighborpixel = lines[n][t]
					if neighborpixel > pixel:
						case = "ohno"
						break
				if case == "ohno": # if there was a greater number in row
					for s in range(0,N):     # check column for numbers
						neighborpixel = lines[s][m]
						if neighborpixel > pixel:
							g.write("Case #" + str(k) + ": " + "NO\n") # CASE NO
							found = True
							break
				if found:
					break
			if found:
				break
		if not found:
			g.write("Case #" + str(k) + ": " + "YES\n") # CASE YES
		k += 1
	f.close()
	g.close()

lawn('B-large.in')
