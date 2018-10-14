with open('B-large.in') as f:
	data = f.readlines()
trials = int(data.pop(0).strip())

for i in range(trials):
	C, F, X = [float(n) for n in data[i].strip().split()]

	rates = [2, 2+F]
	oldTime = X/rates[0]
	newTime = X/rates[1] + C/rates[0]

	while (oldTime > newTime):
		rates.append(rates[-1]+F)
		oldTime = newTime
		newTime += (C-X)/rates[-2] + X/rates[-1]

	print 'Case #{0}: '.format(i+1) + str(oldTime)