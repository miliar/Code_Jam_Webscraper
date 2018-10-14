if __name__ == '__main__' :
	prod = 2

	input = open('B-small-attempt0.in').readlines()

	_T = int(input[0])

	i = 1
	for t in range(1, _T + 1) :
		temp = input[i]
		i += 1
		C = float(temp.split(' ')[0])
		F = float(temp.split(' ')[1])
		X = float(temp.split(' ')[2])

		prod = 2
		time = []
		while True :
			Tc = C  / prod
			Tx = X / prod
			Txf  = X / (prod + F)

			if (sum(time) + Tx <= sum(time) + Tc + Txf) :
				time += [Tx]
				print 'Case #%d: %f' % (t, sum(time))
				break
			else :
				time += [Tc]
				prod += F