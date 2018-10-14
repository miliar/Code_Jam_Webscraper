f = open('input.txt', 'r')
o = open('output.txt', 'w')
case = int(f.readline())

for x in range(case):
	lin = f.readline().split(" ")
	dijk = f.readline()
	dijk = dijk[:len(dijk)-1]
	d2 = ''
	count = 0

	while count < int(lin[1]):
		d2 += dijk
		count+= 1

	final = ''
	minus = 1 

	while len(d2) + len(final) > 3:
		#print d2
		count = 0
		if d2[0] == 'i' and len(final) == 0:
			final += d2[0]
			d2 = d2[1:]
		if d2[0] == 'j' and len(final) == 1:
			final += d2[0]
			d2 = d2[1:]

		if d2[count] == 'i':
			if   d2[count+1] == 'i':
				d2 = d2[2:]
				minus *= -1
			elif d2[count+1] == 'j':
				d2 = 'k'  + d2[2:]
			elif d2[count+1] == 'k':
				d2 = 'j' + d2[2:]
				minus *= -1

		elif d2[count] == 'j':
			if   d2[count+1] == 'i':
				d2 = 'k' + d2[2:]
				minus *= -1
			elif d2[count+1] == 'j':
				d2 = d2[2:]
				minus *= -1
			elif d2[count+1] == 'k':
				d2 = 'i' + d2[2:]

		elif d2[count] == 'k':
			if   d2[count+1] == 'i':
				d2 = 'j' + d2[2:]
			elif d2[count+1] == 'j':
				d2 = 'i' + d2[2:]
				minus *= -1
			elif d2[count+1] == 'k':
				d2 = d2[2:]
				minus *= -1

	if final + d2 == 'ijk' and minus == 1:
		rit = 'YES'
	else:
		rit = 'NO'
	print final + d2, minus
	o.write("Case #" + str(x+1) + ": " + str(rit) + "\n") 
