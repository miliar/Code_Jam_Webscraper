def solve(x):
	digits = [int(z) for z in list(str(x))]

	flag = True

	while True:
		#print(digits)

		for i in range(len(digits)-1):
			if digits[i+1] < digits[i]:
				digits[i] = digits[i]-1
				for j in range(i+1,len(digits)):
					digits[j] = 9
				flag = False
				break
			#print(digits)
			flag = True
		
		if flag:
			break;
			

		


	return int(''.join([str(z) for z in digits]))

with open('input', 'r') as f:
	read_data = f.readlines()

num = int(read_data[0])

with open('output', 'w+') as f:
	for i in range (num):
		toWrite = str(solve(int(read_data[i+1])))
		f.write("Case #" + str(i+1) + ": " + toWrite + "\n")
