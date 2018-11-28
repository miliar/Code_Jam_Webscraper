def pancake(cakes,pan):
	# first from left to right
	totalC = len(cakes)
	newCake = [0]*totalC
	def f(x):
		if x == '+':
			return 1
		else:
			return 0

	newCake = map(f,cakes)

	newCaker = [c for c in newCake]
	newCakel = [c for c in newCake]
	'''
	for i in xrange(totalC):
		if cakes[i] == '+':
			newCake[i] = 1
	'''		
	# second pass
	flipr = 0
	flipl = 0
	rightPos = True
	leftPos = True
	i = 0
	
	while (i < totalC):
		if (newCaker[i] == 0 and ((i + pan - 1) < totalC)):
			for j in xrange(i,i+pan):
				newCaker[j] = 1-newCaker[j]
			flipr += 1
			
		elif (newCaker[i] == 0 and ((i + pan - 1) >= totalC)):
			rightPos = False
			break
		i = i+1
	
	m = totalC-1	
	while (m >= 0):
		if (newCakel[m] == 0 and ((m-pan+1) >=0)):
			for n in xrange(m,m-pan,-1):
				newCakel[n] = 1-newCakel[n]
			flipl += 1
		elif (newCakel[m] == 0 and ((m-pan+1) < 0)):
			leftPos = False
			break
		m -= 1	
	if (leftPos and rightPos):
		result = min(flipl,flipr)
	if (leftPos and (not rightPos)):
		result = flipl
	if (rightPos and (not leftPos)):
		result = flipr
	if (not leftPos and (not rightPos)):
		result = -1	
	return result						
		

T = int(raw_input())
for i in xrange(T):
	S = str(raw_input())
	[cakes,pan] = S.split()
	pan = int(pan)
	result = pancake(cakes,pan)
	if (result >= 0):
		print('Case #{}: {}'.format(i+1, result))
	else:
		print('Case #{}: IMPOSSIBLE'.format(i+1))
		

	





					


			





