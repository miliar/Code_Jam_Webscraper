filename = open('/home/adhitya/Desktop/A-small-attempt0.in')
lines = int (filename.readline())
for line_number,line in enumerate(filename):
	number = int(line[:2])
	value = line[2:]
	total = 0
	additions = 0
	for i in range(number+1):
		if(total<i):
			extra = i-total
			additions+=extra
			total+=extra
		total+=int(value[i])
	print "Case #"+str(line_number+1)+": "+str(additions)
