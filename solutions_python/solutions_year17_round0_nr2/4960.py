n = int(input())
x=0
while x<n:
	number = int(input())
	tidy = False
	while not tidy:
		num_str = str(number)
		ln = len(num_str)
		m=0
		while m<ln-1:
			if int(num_str[m])>int(num_str[m+1]):
				number-=1
				break
			m+=1

		if m==ln-1 and int(num_str[m-1])<=int(num_str[m]):
			tidy = True
	print("Case #%d: %d"%(x+1, number))
	x+=1
