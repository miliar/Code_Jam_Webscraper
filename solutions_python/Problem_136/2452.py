def toBuy(left,spd,fm,es):
	t1 = left/spd
	t2 = (left + fm)/(spd + es)
	return t1 >= t2

data = open('B-large.in','r')
res = open('res2.txt','w')
T = int(data.readline())

for C in range(T):
	vrs = data.readline().split()
	farm = float(vrs[0])
	es = float(vrs[1])
	x = float(vrs[2])
	time = 0
	spd = 2.0
	cookie = 0
	while True:
		if farm >= x:
			time += x/spd
			break
		if cookie < farm:
			time += (farm - cookie)/spd
			cookie = farm
		if toBuy(x-cookie,spd,farm,es):
			cookie -= farm
			spd += es
		else:
			time += (x-cookie)/spd
			break
	res.write('Case #'+str(C+1)+': ' + str(round(time,7))+'\n')
data.close()
res.close()
