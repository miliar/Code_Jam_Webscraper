for t in range(int(raw_input())):
	N = int(raw_input())
	count = 0
	if N<=10:
		count = N
	elif N<=100:
		count = 10 + (N-1)/10 + N-((N-1)/10)*10-1
		if N>20:
			count+=1
	elif N<=1000:
		count = 29 + (N-1)/100+ (N-1)%100
		if N>200:
			count += 1
	elif N<=10000:
		count = 138 + (N-1)/1000+ (((N-1)/100)%10)*10 + (N-1)%100
		if N>1100:
			count += 1
	elif N<=100000:
		count = 138+ 199 + (N-1)/10000+ (((N-1)/1000)%10)*10 + (N-1)%1000
		if N>11000:
			count += 1
	else:
		count = 138 + 199 + 1099+(N-1)/100000+ (((N-1)/10000)%10)*10 + (((N-1)/1000)%10)*100 + (N-1)%1000
		if N>101000:
			count += 1
	print 'Case #%d: %d ' % (t + 1, count)