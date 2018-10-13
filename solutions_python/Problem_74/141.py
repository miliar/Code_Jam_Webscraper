import os

f = open("A-large.in",'r');
g = open("results.dat",'w')
f.readline()

text = f.readlines()
counter = 0;

for line in text:
	counter = counter + 1
	x = line.rstrip().split();
	x = x[1:]
	o=[]
	b=[]
	for i in range(len(x)):
		if (x[i] == 'O'):
			o.append(x[i+1])
		if (x[i] == 'B'):
			b.append(x[i+1])	
	
	o = map(int, o)
	b = map(int, b)
	
	currenttime = 0
	opos = 1
	bpos = 1
	
	
	while (len(x) > 0):
		
		if (x[0] == 'O'):
			timestep = abs(o[0]-opos)+1
			opos = o[0]
			o = o[1:]
			if (len(b) > 0):
				if (abs(b[0] - bpos) < timestep):
					bpos = b[0]
				else:
					if (bpos < b[0]):
						bpos = bpos + timestep
					else:
						bpos = bpos - timestep
		if (x[0] == 'B'):
			timestep = abs(b[0]-bpos)+1
			bpos = b[0]
			b = b[1:]
			if(len(o) > 0):
				if (abs(o[0] - opos) < timestep):
					opos = o[0]
				else:
					if (opos < o[0]):
						opos = opos + timestep
					else:
						opos = opos - timestep
		currenttime = currenttime + timestep
		x = x[2:]
	g.write("Case #" + repr(counter) + ": " + repr(currenttime) + "\n")
			
			