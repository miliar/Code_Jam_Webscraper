counter = 0
file = open("B-large.in", "r")
for line in file.readlines():
	if(counter > 0):
		
		items = line.split(" ")
		n,s,p = int(items[0]),int(items[1]),int(items[2])
		toplimit = 3*p -2
		minlimit = max([3*p - 4, p])
		free, possible = 0, 0
		
		for idx, i in enumerate(items):
			if idx >=3:
				val = int(i)
				if(val >= toplimit):
					free = free + 1
				elif val >= minlimit:
					possible  = possible + 1
		
		free = free + min([s, possible])
		
		print "Case #" + str(counter)  + ": " + str(free)
		
	counter = counter + 1
file.close()