with open('input.in','r') as f:
	lines = f.readlines()
f.close

f = open('output.out','w')

tmp = []
for l in lines:
	try: tmp.append(int(l.strip()))
	except ValueError: tmp.append(l.split())
lines = tmp

T = lines[0]

for t in range(T):
	C = t*10+1
	R1 = lines[C+lines[C]]
	R2 = lines[C+5+lines[C+5]]
	i = 0
	card = ''
	for c1 in R1:
		for c2 in R2:
			if c1 == c2: i += 1; card = c1

	if i == 0: f.write('Case #'+str(t+1)+': Volunteer cheated!\n')
	elif i == 1: f.write('Case #'+str(t+1)+': '+card+'\n')
	else: f.write('Case #'+str(t+1)+': Bad magician!\n')

f.close()
