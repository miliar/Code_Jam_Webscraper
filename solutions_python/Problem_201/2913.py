def ls(i, tab):
	j = i
	
	while (j>0) and (tab[j - 1]): 
		j -= 1
	return i - j

def rs(i, tab):
	j = i
	
	while (j<len(tab) - 1) and (tab[j + 1]): 
		j += 1
	return j - i

def getBetter(tab):
	mini = 0
	maxi = 0
	bi = 0
	for i in range(len(tab)):
		if tab[i]:
			tls = ls(i, tab)
			trs = rs(i, tab)
			tmin = min(tls, trs)
			if mini < tmin:
				mini = tmin
				maxi = max(tls, trs)
				bi = i
			elif(tmin == mini):
				tmax = max(tls, trs)
				if(tmax > maxi):
					maxi = tmax
					bi = i

	return (bi, mini, maxi)
	

N = int(input())

for i in range(N) :
	l = raw_input().split(' ')
	N = int(l[0])
	K = int(l[1])
	
	tab = N*[True]
	for p in range(K - 1):
		tab[getBetter(tab)[0]] = False
		
	l = getBetter(tab)
	r1 = l[1]
	r2 = l[2]
	
	
	print('Case #'+str(i+1)+': '+str(r2) + " " + str(r1))


