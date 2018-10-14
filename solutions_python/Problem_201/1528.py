T = int(raw_input())

for i in range(T):
	N, K = [int(j) for j in raw_input().split()]
	
	if N%2==0:
		value1 = N/2-1
		count1 = 1
		
		value2 = N/2
		count2 = 1
	else:
		value1 = N/2
		count1 = 2

		value2 = 0
		count2 = 0		
	
	count = 1
	inc = 2
	
	while count+inc < K:
		tempValue = 0
		tempCount = 0
		if value1%2==0:
			tempValue = value1/2
			value1 = value1/2 - 1	
			tempCount = count1

		else:
			value1 /= 2
			count1 += count1 		
		
		if value2!=0:
			if value2%2==0:
				count1 += count2
			else:
				count2 = tempCount + 2*count2
			value2 /= 2
		else :
			value2 = tempValue
			count2 = tempCount


		count += inc
		#print count, value1, value2, count1, count2
		inc *= 2
	
	if count==K:
		if value2 == 0:
			value2 = value1
		print "Case #%d: %d %d" % (i+1, value2, value1)	
		continue

	#print count, value1, value2, count1, count2

	if K-count>count2:
		count2 = value1
	else: count2 = value2

	if count2%2==0:
		print "Case #%d: %d %d" % (i+1, count2/2, count2/2-1)
	else:
		print "Case #%d: %d %d" % (i+1, count2/2, count2/2)
