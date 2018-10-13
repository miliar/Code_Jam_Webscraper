T = int(raw_input().strip())

for case in range(1,T+1):
	exist = []
	tobuild = []
	(N,M) = map(int,raw_input().strip().split(' '))
	for n in range(N):
		exist.append(raw_input().strip())
	ex = set(exist)

	count = 0
	for m in range(M):
		ln = raw_input().strip().split('/')
		ln.pop(0)
		rebuild = ''
		for i in range(len(ln)):
			rebuild += "/" + ln[i]
			if rebuild not in ex:
				count += 1
				ex.add(rebuild)
#				print "adding " + rebuild

	print "Case #%d: %d" % (case,count)
