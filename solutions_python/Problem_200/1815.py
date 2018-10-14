ifile = 'B-large.in'
ofile = 'B_l.txt'


out = open(ofile, 'w')

with open(ifile, 'r') as f:
	T = int(f.readline())
	for j in range(1, T+1):
		out.write('Case #%s: ' % j)

		n = int(f.readline())
		p = len(list(str(n))) - 1
		res = n

		index = p
		while index > 0:
			if (n / 10**index) % 10 > (n / 10**(index-1)) % 10:
				break
			else:
				index -= 1

		if index > 0:
			if (n / 10**index) % 10 == 1:
				res = 10**p - 1
			else:  ## need to trace back until valid
				while index < p and (n / 10**index) % 10 == (n / 10**(index+1)) % 10:
					index += 1
				res = n / (10**index) * (10**index) - 1


		out.write('%s\n' % res)
		

out.close()

