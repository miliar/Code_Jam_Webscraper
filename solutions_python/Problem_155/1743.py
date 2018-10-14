f = open('A-large.in.txt', 'r')

T = 0

i = 0
for line in f:
	if (i == 0):
		T = int(line)
	else:
		a = line.split()
		smax = a[0]
		shyness = a[1]
		standing = 0
		friends = 0
		k = 1
		for shy in shyness:
			n = int(shy)
			standing += n
			if (standing < k):
				friends += 1
				standing += 1
			k += 1
		print('Case #' + str(i) + ': ' + str(friends))
	i += 1



f.close()