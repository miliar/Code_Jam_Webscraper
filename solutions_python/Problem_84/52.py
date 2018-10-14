import sys,copy

P = []


n = 0
l = 0
for line in sys.stdin:
	if n == 0:
		n = 1
		continue
	word = line.split()
	if l == 0:
		R = int(word[0])
		C = int(word[1])
		P = []
		l = 1
		continue
	
	if l < (R):
		P += [word[0]]
		l += 1
		continue
	else:
		P += [word[0]]
		nflg = 0
		
		for y in range(R-1):
			for x in range(C-1):
				if P[y][x] == "#"  and P[y][x+1] == "#" and P[y+1][x] == "#"  and P[y+1][x+1] == "#":
					if x!= (C-2):
						P[y] = P[y][:x] + "/\\" + P[y][x+2:]
						P[y+1] = P[y+1][:x] + "\\/" + P[y+1][x+2:]
					elif x!= 0:
						P[y] = P[y][:x] + "/\\"
						P[y+1] = P[y+1][:x] + "\\/"
					else:
						P[y] = "/\\" + P[y][x+2:]
						P[y+1] = "\\/" + P[y+1][x+2:]
		nflg = 0
		for y in range(R):
			for x in range(C):
				if P[y][x] == "#":
					nflg = 1
					break
			if nflg == 1:
				break
		print "Case #" + str(n) + ":"
		if nflg == 1:
			print "Impossible"
		else:
			for y in range(R):
				print P[y]
		l = 0
		n += 1
