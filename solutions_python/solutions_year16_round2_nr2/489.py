def solve(n,casen):
	
	n = n.split()
	num1 = list(n[0])
	num2 = list(n[1])

	l1 = []
	l2 = []

	for i in range(0,len(num1)):
		if num1[i] == '?':
			l1.append(i)

	for i in range(0,len(num2)):
		if num2[i] == '?':
			l2.append(i)


	for i in range(0,len(l1)):
		num1[l1[i]] = '0'

	for i in range(0,len(l2)):
		num2[l2[i]] = '0'




	n1 = []
	n2 = []

	while True:	
		n1.append(int(''.join(num1)))
		i = -1
		flg = False

		while True:

			if i == (-1)*(len(l1)+1):
				flg = True
				break;

			if num1[ l1[i]  ] != '9':
				num1[ l1[i]  ] = chr(ord(num1[ l1[i]  ])+1)
				break;
			else:
				num1[ l1[i]  ] = '0'
				i = i - 1

		if flg:
			break;

	while True:	
		n2.append(int(''.join(num2)))
		i = -1
		flg = False

		while True:

			if i == (-1)*(len(l2)+1):
				flg = True
				break;

			if num2[ l2[i]  ] != '9':
				num2[ l2[i]  ] = chr(ord(num2[ l2[i]  ])+1)
				break;
			else:
				num2[ l2[i]  ] = '0'
				i = i - 1

		if flg:
			break;


	# print n2,n1

	minimum = abs(n1[0] - n2[0])
	ans1 = n1[0]
	ans2 = n2[0]


	for i in n1:
		for j in n2:
			if minimum > abs(i-j):
				minimum = abs(i-j)
				ans1 = i
				ans2 = j



	print "Case #"+str(casen)+":",format(ans1, "0"+str(len(n[0]))+"d"),format(ans2, "0"+str(len(n[1]))+"d")

t = int(raw_input())
for i in xrange(1, t + 1):
	n = raw_input()
	solve(n,i)