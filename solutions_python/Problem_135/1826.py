F = open('A-small-attempt0.in').read()

f = F.split('\n')
T = f[0]

for t in range(0,int(T)):
	fl = (t*10)+1
	first = int(f[fl])
	fa = f[fl+first].split()
	#print fa

	sl = (t*10)+6
	second = int(f[sl])
	sa = f[sl+second].split()
	#print sa

	c = 0
	for fr in fa:
		for sr in sa:
			if(fr == sr):
				c += 1
				v = fr
	if(c == 1):
		ans = v
	elif(c > 1):
		ans = "Bad magician!"
	elif(c == 0):
		ans = "Volunteer cheated!"

	print "Case #"+str(t+1)+": "+ans


