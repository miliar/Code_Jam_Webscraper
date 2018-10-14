t = input()

for qe in range(1, t+1):
	
	s = [ord(i) - ord('0') for i in raw_input()]

	flag = True

	while flag:
		flag = False
		for i in range(len(s)-1):
			if s[i] > s[i+1]:
				for j in range(i+1, len(s)):
					s[j] = 9
				s[i] -= 1
				flag = True
				break


	print 'Case #{}: {}'.format(qe, int(''.join(str(i) for i in s)))