
fo = open('outputLarge', 'w')


lines = [line.strip() for line in open('B-large.in')]
input = lines;



for x in range(0,int(input[0])):
	arrline = input[x+1].split(' ')
	
	cp = round(float(arrline[0]),5) #initial
	fp = round(float(arrline[1]),5) #farm
	xp = round(float(arrline[2]),5) #cookies to win
	cookies = 0
	tp = 0
	f = 0
	t = 0
	tf = 0
	rate = 0

	while cookies < xp :

		rate = 2 + (f*fp)
		tf = cp / rate

		dt = float((xp / rate))
		dt2 =  float((xp / (rate+fp))) + tf

		if (cp + cookies) >= xp :
			t = float(xp / rate)
			cookies = xp
		else :
			if dt  > dt2 :
				cookies = 0
				t = t + tf
				f += 1
			else :
				t = t + dt
				cookies = xp
	pass
	r = ("{:1.7f}".format(t))
	txt = ("Case #%d: %s" % ((x+1),r))
	fo.write(txt+"\n")

fo.close()