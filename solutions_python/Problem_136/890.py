with open('input.in','r') as f:
	lines = f.readlines()
f.close

f = open('output.out','w')

tmp = []
for l in lines:
	try: tmp.append(int(l.strip()))
	except ValueError: tmp.append([float(f) for f in l.split()])
lines = tmp

T = lines[0]

for case in range(1,T+1):
	C_per_sec = 2.0
	C,F,X = lines[case]
	s = 0
	while 1:
		if (X-C)/C_per_sec < X/(C_per_sec+F):
			s += X/C_per_sec
			break
		else:
			s += C/C_per_sec
			C_per_sec += F
	f.write('Case #'+str(case)+': '+str(s)+'\n')
