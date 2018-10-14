import sys

def cat(filename):
        lines = []
        with open(filename) as f:
                for line in f:
                        line = line.replace("\n","")
                        lines.append(line)
        return lines

def action(m):
	icount = 0
	flipped = 0
	while(flipped == 0):
		result = ""
		string = m.split(" ")

		size = int(string[1])
		panc = string[0]

		flipped = {}
		fcount = 0
		compstring = ""
		for p in panc:
			flipped[fcount] = p
			fcount = fcount + 1
			compstring = compstring + "+"


		if(panc == compstring):
			return icount
			break
		else:
			try:
				pcount = 0
				for r in range(len(panc)):
					if flipped[pcount] == "-":
						for c in range(size):
							if flipped[pcount+c] == "-":
								flipped[pcount+c] = "+"
							else:
								flipped[pcount+c] = "-"
						icount = icount + 1
					pcount = pcount + 1
			except:
				result = "IMPOSSIBLE"
		if result == "IMPOSSIBLE":
			return result
			break
		else:
			pcount = 0
			for r in range(len(panc)):
				result = result + flipped[pcount]

			return icount

		icount = icount + 1


if len(sys.argv) > 1:
        inp = cat(sys.argv[1])
        caseNum = 1

        for i in range(len(inp)-1):
                n = inp[i+1]

                output = action(n)

                print("%s%d%s%s" % ("Case #", caseNum, ": ", str(output)))
                caseNum = caseNum + 1

else:
        print
        print "Please provide a file name for input. \n ( Example: python <script> <input filename> )"
        print

