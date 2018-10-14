T = input()



for t in range(T):
	N = input()
	vines = list()

	for n in range(N):
		data = raw_input().split()
		vines.append([int(data[0]),int(data[1]),0])

	vines[0][2] = vines[0][0]

	totaldistance = input()

	complete = False
	for itr,val in enumerate(vines):
		if vines[itr][2] == 0: continue
		for i in xrange(itr+1,len(vines)+1):			
			if vines[itr][2] + vines[itr][0] >= totaldistance:
				complete = True
				break

			if i == len(vines): break
			distance = vines[i][0] - vines[itr][0]
			if vines[itr][2] < distance: break



			diameter = min(distance,vines[i][1])
			if diameter <= vines[i][2]: continue
			else: vines[i][2] = diameter

		if complete: break

	#print vines,totaldistance
	if complete:
		print("Case #%d: %s" % (t+1,"YES"))
	else:
		print("Case #%d: %s" % (t+1,"NO"))