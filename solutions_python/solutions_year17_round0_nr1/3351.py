t = int(raw_input())
for i in range(1,t+1):
	pancakeRow = raw_input().split(" ")
	strPancakeRow,flipper = pancakeRow
	strPancakeRow = list(strPancakeRow)
	possible = True
	flips = 0
	if len(strPancakeRow) < int(flipper):
		for k in range(0,len(strPancakeRow)):
			if strPancakeRow[k] == '-':
				possible = False
	else:	
		for j in range(0,(len(strPancakeRow)-int(flipper)+1)):
			if strPancakeRow[j] == '-':
				for k in range(j,j+int(flipper)):
					if strPancakeRow[k] == '+':
						strPancakeRow[k] = '-'
					else:
						strPancakeRow[k] = '+'
				flips += 1
			if j == len(strPancakeRow)-int(flipper):
				for k in range(0,int(flipper)):
					if strPancakeRow[j+k] == '-':
						possible = False
	if possible:
		print "CASE #%d: %d" % (i,flips)
	else:
		print "CASE #%d: IMPOSSIBLE" % (i)

