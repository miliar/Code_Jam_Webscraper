T = int(raw_input())

for case in xrange(T):
	N = int(raw_input())
	
	naomis = map(float, raw_input().strip().split())
	kens = map(float, raw_input().strip().split())
	
	naomis.sort()
	kens.sort()
	kensd = kens[:]

	#print naomis
	#print kens
	
	warscore = 0
	for s in naomis[::-1]:
		if s < kens[-1]:
			kens.remove(kens[-1])
		else:
			warscore+=1
			kens.remove(kens[0])
	
	dwarscore = 0
	for s in naomis:
		if s < kensd[0]:
			kensd.remove(kensd[-1])
		else:
			dwarscore+=1
			kensd.remove(kensd[0])
				
	print 'Case #'+str(case+1)+':',dwarscore,warscore