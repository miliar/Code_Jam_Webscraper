def enterPassword(passy):
	bpos = 1
	opos = 1
	g = 0
	seconds = 0
	for step in range(len(passy)):
		c = passy[step][0]
		if c == "O": g = abs(opos - passy[step][1]) + 1
		else: g = abs(bpos - passy[step][1]) + 1
		n = 0
		temp = passy[step+1:]
		for nextstep in range(len(temp)):
			if temp[nextstep][0] != c:
				n = temp[nextstep][1]
				break
		if c == "O":
			seconds += abs(opos - passy[step][1]) + 1
			opos = passy[step][1]
			if bpos > n:
				bpos -= g
				if bpos < n and n != 0:
					bpos = n
			elif bpos < n:
				bpos += g
				if bpos > n and n != 0:
					bpos = n
		else:
			seconds += abs(bpos - passy[step][1]) + 1
			bpos = passy[step][1]
			if opos > n: 
                                opos -= g
                                if opos < n and n != 0:
                                        opos = n
                        elif opos < n:
                                opos += g
                                if opos > n and n != 0:
                                        opos = n

	return seconds



def parseFile(input):
	f = open(input, "r")
	totalCases = int(f.readline().rstrip())
	fo = open("output.txt", "w")
	for i in range(totalCases):
		line = f.readline().rstrip()
		r = []
		line = line[2:].split()
		for x in range(0, len(line), 2):
			y = [line[x], int(line[x+1])]
			r.append(y)
		fo.write("Case #" + str(i+1) + ": " + str(enterPassword(r)) + "\n")
	f.close()
	fo.close()
			
			
if __name__ == "__main__":
	import sys
	parseFile(sys.argv[1])
