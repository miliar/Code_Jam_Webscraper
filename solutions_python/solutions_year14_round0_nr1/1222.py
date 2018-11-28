

for case in xrange(input()):
	r1 = int(input())
	data1 = []
	for i in xrange(r1):
		data1 = map(int, raw_input().split(' '))
	for i in xrange(r1, 4):
		raw_input()
	r2 = int(input())
	data2 = []
	for i in xrange(r2):
		data2 = map(int, raw_input().split(' '))
	for i in xrange(r2, 4):
		raw_input()
	
	sol = 0
	numero = 0
	for j in xrange(4):
		z = 0
		while (z<4) and (data2[z] != data1[j]):
			z+=1
		if (z <4) and (data2[z] == data1[j]):
			sol += 1
			numero = str(data1[j])
	if (sol == 0):
		numero = 'Volunteer cheated!'
	elif (sol > 1):
		numero = 'Bad magician!'

	print 'Case #%d: %s' % ((case+1), numero)

