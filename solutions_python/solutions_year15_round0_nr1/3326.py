infile = open('inputfile', 'r')
index = 0
result = 0
sofar = 0
req = 0

for line in infile:
	if index==0:
		index +=1
	else:
		result = 0
		sofar = 0
		req = 0
		los = line.split()
		maxi = int(los[0])
		lis  = los[1]
		for c in lis:
			if req > sofar:
				diff = req-sofar
				result += diff
				req +=1
				sofar +=diff+int(c)
			else:
				req += 1
				sofar += int(c)
		outfile = open('outputfile', 'a')
		outfile.write('Case #'+str(index)+': '+str(result)+'\n')
		index += 1	
