t = int(input().strip())
for test in range(t):
	s = list(input().strip())
	for i in reversed(range(1,len(s))):
		if s[i-1] > s[i] :
			s[i-1] = chr(int(s[i-1]) - 1 + ord('0'))
			for j in range(i, len(s)):
				s[j] = '9'
	j = 0
	while s[j] == '0' :
		j+=1
	print("Case #", test+1, ": ", end = '', sep = '')
	for k in range(j, len(s)):
    	
		print(s[k], end = '')
	print()