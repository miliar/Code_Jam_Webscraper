in_file = open("4.txt")

t= int (in_file.readline().strip() )

def war(one , two):
	while len(one) > 0:
		found = False
		for thing in two:
			if thing >= one[0]:
				two.remove(thing)
				one = one[1:]
				found = True
				break
		if found == False:
			return len(one)
	return 0

def deceit( one , two):
	n_s = 0
	while len(one) > 0:
		if one[0] > two[-1]:
			n_s += len(one)
			break

		elif one[0] > two[0]:
			n_s += 1
			one = one[1:]
			two = two[1:]

		elif one[0] < two[-1]:
			one = one[1:]
			two = two[:-1]

		
	return n_s


for z in range(t):

	n = int( in_file.readline().strip() )

	nao = in_file.readline().strip().split()
	ken = in_file.readline().strip().split()

	for i in range(n):
		nao[i] = float( nao[i] )
		ken[i] = float( ken[i] )

	nao.sort()
	ken.sort()
	#print nao
	#print ken
	temp1 = nao[:]
	temp2 = ken[:]
	#print temp1,temp2
	one =  war(temp1,temp2)
	temp1 = nao[:]
	temp2 = ken[:]
	#print temp1,temp2
	two =  deceit(temp1,temp2)
	print "Case #{}: {} {}".format(z+1,two,one)



'''
	for i in range(len(one) - 1, -1 , -1):
		if one[i] > two[-1]:
			one = one[:i] + one[i+1:]
			two = two[1:]
			n_s += 1
		else:
			break
'''