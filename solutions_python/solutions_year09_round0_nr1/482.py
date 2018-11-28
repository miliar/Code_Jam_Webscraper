f = open('A-large.in', 'r')

first_line = f.readline()
first_line_list = first_line.split(' ')
L = int(first_line_list[0])
D = int(first_line_list[1])
N = int(first_line_list[2])

d_list = list()
n_list = list()

for i in range(1, D+1):
	d_list.append(f.readline())

for i in range(D+2, D+2+N):
	n_list.append(f.readline())

#print L
#print D
#print N
#print d_list
#print n_list

for i in range(N):
	count = 0
	index = 0
	inside = False
	asdf = n_list[i]

	a_list = list()

	for j in range(len(asdf)-1):
		qwer = asdf[j]
		a_list.append(list())

		if qwer == '(':
			inside = True
			continue
		elif qwer == ')':
			inside = False
			index = index + 1
			continue
		else:
			a_list[index].append(qwer)
			if not inside:
				index = index + 1

	for j in range(D):
		asdf = d_list[j]

		passed = True

		for k in range(L):
			if asdf[k] not in a_list[k]:
				passed = False
		if passed:
			count = count + 1
			
	print "Case #" +  str(i+1) + ": " + str(count)







