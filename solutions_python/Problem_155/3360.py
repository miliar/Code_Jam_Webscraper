f = open('/home/abhibel/Downloads/A-large.in', 'r')

cases = int(f.readline())
i = 1

while cases>=i:
	line = f.readline()
	lines = line.split(" ")
	maxshy = lines[0].strip(" ")
	people = lines[1].strip("\n")
	length = len(people)
	if length==1:
		print ("Case #" + str(i) + ": " + str(0))
	else:
		count = 0
		tot = 0
		req = 0
		for p in people:
			if int(p)==1:
				count+=1
		if count==length:
			print ("Case #" + str(i) + ": " + str(0))
		else:
			maxi = 0
			for p in people:
				req+=1
				tot+=int(p)
				if tot<req:
					diff = req - tot
					if maxi<diff:
						maxi =  diff
					#print(maxi)
			print ("Case #" + str(i) + ": " + str(maxi))			
	i+=1
