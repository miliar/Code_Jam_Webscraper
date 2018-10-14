def isTidy(nb):
	t=str(nb)
	old = int(t[0])
	res = True
	i = 0
	while (i<len(t)) and (res): 
		if(int(t[i]) < old):
			res = False
		old = int(t[i])
		i=i+1
	return res

N = int(input())

for i in range(N) :
	nb=int(input())
	index = 0
	while(not isTidy(nb)):
		t=str(nb)
		if(t[index] >= t[index + 1]):
			nb = nb - int(t[index + 1 : len(t)]) - 1
		index += 1
		
	print('Case #'+str(i+1)+': '+str(nb))


