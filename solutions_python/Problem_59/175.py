T = int(raw_input())

for t in range (1,T+1):
	(N,M) = map(int,raw_input().split())
	
	existingPaths = []
	toCreatePaths = []
	completePaths = []
	
	for i in range(0,N):
		existingPaths.append(raw_input())
		
	for i in range(0,M):
		toCreatePaths.append(raw_input())
		
	for existingPath in existingPaths:
		while existingPath != '' :
			completePaths.append(existingPath)
			existingPath = existingPath[:existingPath.rfind('/')]
	
	directoriesCreatedCount = 0
	for existingPath in toCreatePaths:
		while existingPath != '' :
			if existingPath not in completePaths:
				directoriesCreatedCount += 1
				completePaths.append(existingPath)
			existingPath = existingPath[:existingPath.rfind('/')]
			
	print "Case #%d: %d" % (t,directoriesCreatedCount)