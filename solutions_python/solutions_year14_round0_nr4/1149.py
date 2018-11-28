test = int(input())
for i in range(1,test+1):
	count = int(input())
	noami = list(map(float,input().split()))
	ken = list(map(float,input().split()))
	noami.sort()
	ken.sort()
	war = 0
	dec = 0
	en = count -1
	st = 0
	j = count -1
	while j >= 0:
		if noami[j] > ken[en]:
			war= war+1
		else:
			en = en -1
		j = j-1
	en = count -1
	j = 0 
	k = count -1
	while k >= 0:
		if noami[j] > ken[st]:
			dec = dec+1
			st = st + 1
		else:
			en = en -1
		k = k -1
		j = j +1
	print("Case #"+str(i)+": "+str(dec)+" "+str(war))
	
			
		
