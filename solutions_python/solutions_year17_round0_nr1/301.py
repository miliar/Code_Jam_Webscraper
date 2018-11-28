
data = open('A-large.in', 'r').readlines()
n = int(data[0])
answ = []
for i in range(n):
	happy, k = data[i + 1].split()
	happy = [x == '+' for x in happy]
	k = int(k)
	flips = 0
	for j in range(len(happy) - k + 1):
		if not happy[j]:
			flips += 1
			for z in range(k):
				happy[j + z] = not happy[j + z]
	if all(happy):
		answ.append(flips)
	else:
		answ.append('IMPOSSIBLE')

with open('A-large.out', 'w') as f:
    for i, o in enumerate(answ):
        f.write('Case #{}: {}\n'.format(i+1, o))
