def palindrome(num):
	if(num<10):
#		print "single digit"
		return 1
	
	s = str(num)
	length = len(s)
	#print s
	i=0
	result = 1
	halflenth = length/2
#	print "length  and halflength ",
#	print length,
#	print halflenth
	while(i<halflenth):
		if(s[i]!=s[length-i-1]):
			result=0
			return result
		i=i+1
	
	return result
