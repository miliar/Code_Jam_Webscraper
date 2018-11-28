T = int(raw_input())

for re in range(T):
	s = '0' + raw_input().strip()
	s = list(s)
	n = len(s)
	done = False
	for i in range(n - 1):
		if s[i] > s[i+1]:
			j = i
			while s[j-1] == s[i]:
				j -= 1
			s[j] = chr(ord(s[j]) - 1)
			j += 1
			while j < n:
				s[j] = '9'
				j += 1
			break
	print 'Case #' + str(re+1) + ': ' + ''.join(s).strip('0')

