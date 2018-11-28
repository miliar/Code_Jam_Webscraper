t = int(input())

for test_case in range(t):
	num = list(str(input()))
	#print (num)
	place = -1
	N = len(num)
	for i in reversed(range(1, N)):
		if (num[i - 1] > num[i]):	
			num[i - 1] = str(int(num[i - 1]) - 1)
			for j in range(i, N):
				num[j] = "9"
	
	while True:
		#print(num[0])
		if (num[0] != '0'):
			break
		num.pop(0)

		
	res = "".join(num)
	print ("Case #{0}: {1}".format(test_case + 1, res))