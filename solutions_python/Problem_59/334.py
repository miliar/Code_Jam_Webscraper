for e in range(int(raw_input())):
	a = raw_input().split()
	limits = [int(x) for x in a]
	root = {}
	for x in range(limits[0]):
		directory = raw_input().split('/')
		tmp = root
		for dire in directory:
			if dire!='':
				if dire not in tmp:
					tmp[dire]={}
					tmp = tmp[dire]
				else:
					tmp = tmp[dire]
	comNum = 0
	for x in range(limits[1]):
		newDir = raw_input().split('/')
		tmp = root
		for dire in newDir:
			if dire!='':
				if dire not in tmp:
					tmp[dire]={}
					comNum+=1
					tmp = tmp[dire]
				else:
					tmp = tmp[dire]
	print "Case #%d: %d" % (e+1,comNum)

