incantation = {"combos": [], "oppositions": [], "chant": [], "chantlength": 0}

def doMagicalness():
	k = list(incantation["chant"])
	for e in range(incantation["chantlength"]):
		if e == 0: continue
		c1 = k[e]
		c2 = k[e-1]
		#search for combo
		for [cb, nu] in incantation["combos"]:
			if cb == c1 + c2 or cb == c2 + c1:
				k[e] = nu
				k[e-1] = "-"
				c1 = "-"
		for j in range(e):
			if c1 == "-": break
			m = e - j - 1
			for perhaps in incantation["oppositions"]:
				if perhaps == c1 + k[m] or perhaps == k[m] + c1:
					for l in range(e+1):
						k[l] = "-"
	for i in range(k.count("-")):
		k.remove("-")
	return k;






def processFile(input):
	f = open(input, "r")
	fo = open("output.txt", "w")
	testCases = int(f.readline().rstrip())
	for i in range(testCases):
		r = f.readline().rstrip().split()
		mmmm = int(r[0])
		brrr = 0
		l = []
		j = 0
		for j in range(mmmm):
			l.append((r[brrr + j + 1][0:2], r[brrr + j + 1][2]))
		if mmmm == 0: brrr += 1
		else: brrr += j + 2
		incantation["combos"] = l
		l = []
		mmmm = int(r[brrr])
		for j in range(mmmm):
			l.append(r[brrr + j + 1])
                if mmmm == 0: brrr += 1    
                else: brrr += j + 2
		incantation["oppositions"] = l
		incantation["chantlength"] = int(r[brrr])
		incantation["chant"] = r[brrr + 1]
		t = doMagicalness()
		fo.write("Case #" + str(i + 1) + ": [" + ", ".join(t) + "]\n")




if __name__ == "__main__":
	import sys
	processFile(sys.argv[1])
