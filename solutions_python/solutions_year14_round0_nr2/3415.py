output = ""

def cookies(c, f, x):
	"""
		c - cost of farm
		f - production of cookies per second for one farm
		x - goal to reach
	"""
	cookies = 0
	production = 2
	p = production
	
	t1 = x / p
	it = 1
	
	while True:
		p = 2
		t2 = 0
		for i in range(it):
			t2 += c / p
			p += f
		t2 += x / p
		
		if t1 < t2: return t1
		
		t1 = t2
		it += 1
		
		
		#s1 = c / p # seconds needed for new farm
		#s2 = x / p # seconds needed for winning the game
		#s3 = c / (p + f)
		#if (s2 < s1 + s3): return time + s2
		#time += s1
		

T = int(input()) # number of tricks
for i in range(1, T + 1):
	line = input()
	(C, F, X) = list(map(float, line.split(" ")))
	
	res = round(cookies(C, F, X), 7)
	
	print("Case #", i, ": ", res, sep = "")

print(output)

