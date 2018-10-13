tc = int(input())
count = 1
while tc:
	n = input()
	temp = int(n)
	while temp:
		flag = True
		strn = str(temp)
		for i in range(len(strn) - 1):
			if int(strn[i]) > int(strn[i + 1]):
				flag = False
				break

		if flag:
			print("Case #", count, ": ", temp, sep = '')
			break
		else:
			temp -= 1
	count += 1
	tc -= 1