#f = file("problem3test.in", "r")
#f = file("/Users/finn/Downloads/C-small-attempt0.in", "r")
#f = file("/Users/finn/Downloads/C-small-attempt1.in", "r")
#f = file("/Users/finn/Downloads/C-small-attempt2.in", "r")
f = file("/Users/finn/Downloads/C-large.in", "r")
#of = file("C-small.out", "w")
of = file("C-large.out", "w")
lines = f.readlines()

cases = int(lines[0])
line = 1
for case in range(cases):
	n = int(lines[line])
	line += 1
	
	candies = []
	for v in lines[line].split():
		candies.append(int(v))
	line += 1
		
	candies.sort()
	
	sum = 0
	xor_sum = 0
	for c in candies:
		sum += c
		xor_sum ^= c
		
	if xor_sum == 0:
		maxval = sum
		
		if len(candies) >= 1:
			maxval -= candies[0]
			
		result = str(maxval)
	else:
		result = "NO"	
	
	of.write("Case #%d: %s\n" % (case + 1, result))
	
