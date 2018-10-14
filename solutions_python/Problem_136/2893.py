fin = open("B-large.in", "r");

t = int(fin.readline());

for i in range(1, t+1):
	c, f, x = [float(n) for n in fin.readline().split(" ")];
	cps = 2;
	time = 0;
	
	while True:
		ttf = c/cps;
		ttw = x/(cps+f);
		#print cps, ttf, ttw, ttf+ttw, x/cps
		
		if (ttf+ttw) < (x/cps):
			time += ttf; #make farm
			cps += f;
		else:
			time += x/cps; #make farm
			break;
	
	time = round(time, 7);
	print "Case #" + str(i) + ": " + str(time);
	