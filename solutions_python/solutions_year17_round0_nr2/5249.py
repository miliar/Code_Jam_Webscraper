fname = 'B-small-attempt0.in'

txt = []	# to read the lines from file
c = []		# to store the digits
		
with open(fname) as f:
	for line in f:
		txt.append(line.rstrip())
		
	T = int(txt[0])
	
	for i in range(1,len(txt)):
		n = int(txt[i])
		st = txt[i]
		result = True		# to break the loop
		while result == True:
			for digit in st:
				c.append(int(digit))	# store the digits to compare later
			#print(c)
				
			if sorted(c) == c:	# check if sorted number is equal which means its tidy
				c = []
				result = False
			else:
				n = n - 1
				st = str(n)
				c = []
				
		print("Case #" + str(i) + ": " + st)
