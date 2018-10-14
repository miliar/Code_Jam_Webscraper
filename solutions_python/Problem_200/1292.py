t = int(input())
for tc in range(t):
	
	s = input()
	ans = ""
	for i in range(len(s)):
		digit = int(s[i])
		greater = True
		for j in range(i+1, len(s)):
			if int(s[j]) != digit:
				greater = False
			
		for j in range(i+1, len(s)):
			if int(s[j]) > digit:
				greater = True
				break
			if int(s[j]) < digit:
				break
		
		
		if greater:
			ans += str(digit)
		else:
			ans += str(digit-1)
			for j in range(i+1, len(s)):
				ans += '9'
			break
				
			
		
	
	
	print ('Case #', (tc+1), ': ', int(ans), sep='')
