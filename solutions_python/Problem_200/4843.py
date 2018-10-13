t = int(input(""))
for t1 in range(1, t + 1):
	no = int(input(""))
	i = no
	while(i > 0):
		flag = 0
		temp = i
		prevDigit = temp % 10
		temp /= 10
		while(temp > 0):
			nextDigit = temp % 10
			if(prevDigit < nextDigit):
				flag = 1
			prevDigit = nextDigit
			temp = temp / 10
		if(flag == 0):
			tidy = i
			break;
		i -= 1;
	print "Case #%d: %d" % (t1, tidy);