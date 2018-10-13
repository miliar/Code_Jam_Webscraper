with open('A-large.in') as f:
	with open('A.out', 'w') as out:
		tests = f.readline()
		testNum = 1
		for line in f:
			vals = line.split(" ")
			max = vals[0]
			cur = vals[1].strip()
			total = 0
			count = 0
			need = 0
			for chr in cur:
				if total >= count:
					total = total + int(chr)
				else:
					need = need + (count - total)
					total = count + int(chr)
				count += 1
			out.write("Case #" + str(testNum) + ": " + str(need) + "\n")
			testNum += 1
		