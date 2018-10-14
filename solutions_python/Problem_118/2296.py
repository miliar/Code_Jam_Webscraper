import math
t = long(raw_input())
for i in range(t):
	counting = 0
	iput = raw_input()
	y = iput.split()
	a = long(y[0])
	b = long(y[1])
	for j in range(a,b+1):
		strin = str(j)
		x = 0
		y = len(strin)-1		
		while(x-y<=0):
			if strin[x] == strin[y]:
				x += 1
				y -= 1
				f = 1
			else:
				f =0
				break
		if f == 1:	
			strin1 = math.sqrt(j)
			if strin1 == int(strin1):
				strin1 = str(int(strin1))
				x = 0
				y = len(strin1)-1		
				while(x-y<=0):
					if strin1[x] == strin1[y]:
						x += 1
						y -= 1
						f1 = 1
					else:
						f1 =0
						break
				if f1 == 1:
						counting += 1
	print "Case #%i: %i"%(i+1,counting)
