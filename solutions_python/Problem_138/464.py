T = int(raw_input())
for x in range(T):
	N = int(raw_input())
	naomi = map(float,raw_input().split())
	ken = map(float,raw_input().split())
	naomi.sort()
	ken.sort()
	
	war = N
	nao = 0
	K = 0
	while K<N:
		if naomi[nao] < ken[K]:
			war = war - 1
			nao = nao+1
			K = K + 1
		else:
			K = K + 1
			
	dWar = N
	nao = 0
	K = 0
	kMax = N
	while K < kMax:
		if naomi[nao] < ken[K]:
			dWar = dWar - 1
			nao = nao+1
			kMax = kMax - 1
		else:
			K = K + 1
			nao = nao+1
					
	
	
	answer = "hi there"
	print "Case #"+str(x+1)+": "+str(dWar) + " " + str(war)
