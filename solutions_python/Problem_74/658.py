import sys

fi = open("input.txt", "r")
fo = open("output.txt", "w")

c = int(fi.readline().strip());
for tc in range(1, c + 1):
	tmp = list(map(str, fi.readline().strip().split(" ")))
	n = int(tmp[0])

	ans = 0

	o = []
	b = []
	seq = []
	for i in range(1, 2*n):
		if tmp[i] == 'O':
			o.append(int(tmp[i + 1]))
		else:
			if tmp[i] == 'B':
				b.append(int(tmp[i + 1]))
		if tmp[i] == 'O' or tmp[i] == 'B':
			seq.append(tmp[i])
			seq.append(int(tmp[i + 1]))
	o.append(-1)
	b.append(-1)
		
	curr = 0
	currO = 0
	currB = 0
	xo = 1
	xb = 1
	while curr < n:
		if seq[2*curr] == 'O' and abs(xo - seq[2*curr + 1]) >= 0:
			if abs(xo - seq[2*curr + 1]) == 0:
				curr = curr + 1
				currO = currO + 1
			else:
				if xo < seq[2*curr + 1]: xo = xo + 1
				else: xo = xo - 1
			
			if abs(xb - b[currB]) > 0:
				if xb < b[currB]: xb = xb + 1
				else: xb = xb - 1
		else:
			if seq[2*curr] == 'B' and abs(xb - seq[2*curr + 1]) >= 0:
				if abs(xb - seq[2*curr + 1]) == 0:
					curr = curr + 1
					currB = currB + 1
				else:
					if xb < seq[2*curr + 1]: xb = xb + 1
					else: xb = xb - 1
				
				if abs(xo - o[currO]) > 0:
					if xo < o[currO]: xo = xo + 1
					else: xo = xo - 1
		
		ans = ans + 1
						
	fo.write("Case #{0}: {1}\n".format(tc, str(ans)))
	
fi.close()
fo.close()