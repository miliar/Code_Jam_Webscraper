a = open('a.in').read().strip()
outp = open('a.out','wt')
b = a.split('\n')
case = int(b[0].strip())
def portal(somestr):
	bluestat = 0
	orangestat = 0
	bluesite = 1
	orangesite = 1
	s = somestr.split(' ')
	num = int(s[0])
	for k in range (1,num+1):
		if (s[(2*k-1)] == 'B'):
			temp = int(s[2*k])
			bluestat = bluestat + (abs(temp - bluesite) + 1)
			if (bluestat <= orangestat):
				bluestat = orangestat + 1	
			bluesite = temp
		else:
			temp = int(s[2*k])
			orangestat = orangestat + (abs(temp - orangesite) + 1)
			if (orangestat <= bluestat):
				orangestat = bluestat + 1
			orangesite = temp
	return max(bluestat, orangestat)
			
for k in range(1,case+1):
	port = portal(b[k])
	thestr = "Case #"+str(k)+": "+str(port)+"\n"
	outp.write(thestr)
outp.close()

