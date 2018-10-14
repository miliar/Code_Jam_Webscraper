infile = open('A-small-attempt2.in')
ofile = open('result1.txt','w')
line = infile.readline()
line = line.strip('\n')
T = int(line)
for k in range(T):
	strSet = set()
	cntlist = []
	maxvec = []
	isF = True
	isFail = False
	isOnly = False
	line = infile.readline().strip('\n')
	N = int(line)
	if N == 1:
		isOnly = True
	for i in range(N):
		line = infile.readline().strip('\n')
		if isFail or isOnly:
			continue
		pch = line[0]
		tline = line[0]
		cntvector = [1]
		idx = 0
		for j in range(1, len(line)):
			if pch == line[j]:
				cntvector[idx] += 1
				continue
			else:
				tline += line[j]
				pch = line[j]
				cntvector.append(1)
				idx+=1
		cntlist.append(cntvector)
		if isF:
			isF = False
			strSet.add(tline)
			maxvec = [0]*len(cntvector)
			continue
		if tline not in strSet:
			isFail = True
		if isFail == False:
			for li in range(len(maxvec)):
				if cntvector[li] > maxvec[li]:
					maxvec[li] = cntvector[li]
	if isFail:
		ofile.write('Case #%d: Fegla Won\n' % (k+1))
		continue
	if isOnly:
		ofile.write('Case #%d: 0\n' % (k+1))
		continue
	minl = 9999999999
	idx = 0
	refvec = [1]*len(maxvec)
	while idx < len(maxvec):
		ssum = 0
		for ci in range(len(cntlist)):
			for li in range(len(maxvec)):
				ssum += abs(cntlist[ci][li] - refvec[li])
		if ssum < minl:
			minl = ssum
		if refvec[idx] == maxvec[idx]:
			idx += 1
		else:
			refvec[idx] += 1
	ofile.write('Case #%d: %d\n' % (k+1, minl))
