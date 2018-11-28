for e in range(int(raw_input())):
	okna = []
	for x in range(int(raw_input())):
		para = [int(x) for x in raw_input().split()]
		okna.append(para)
	okna.sort(lambda x,y: x[0]-y[0])
	cross = 0
	for x in range(len(okna)):
		for y in range(x,len(okna)):
			if okna[x][1]>okna[y][1]:
				cross+=1
	print "Case #%d: %d" % (e+1,cross)
