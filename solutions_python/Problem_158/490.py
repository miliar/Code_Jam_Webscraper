fin = open("q4.in","r")
fout = open("q4.out","w")

def dosomething(x, r, c):

	if x == 1:
		return "GABRIEL"
	if x == 2:
		if (r * c) % 2 == 0 and r * c >= 2:
			return "GABRIEL"
		else:
			return "RICHARD"
	if x == 3:
		if (r >= 2 and c >= 2) and (r * c) % 3 == 0:
			return "GABRIEL"
		else:
			return "RICHARD"
	if x == 4:
		if r > c:
			r, c = c ,r

		print (r, "  ", c)
		if r < 3: 
			return "RICHARD"
		else:
			if r == 3 and c == 3:
				return "RICHARD"
			else:
				return "GABRIEL"

n = int (fin.readline())
lines = list(fin)

for i in range(n):
	#print (lines[i][2:-1])
	line =  lines[i].split()
	line = map(int, line)
	fout.write("Case #" + repr(i + 1) + ": " + \
	 dosomething(*line) + "\n")
