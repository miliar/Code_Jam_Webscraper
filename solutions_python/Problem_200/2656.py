import codejam as gcj

T = gcj.read_input('i')
for t in range(T):
	N = gcj.read_input('s')
	digits = [int(d) for d in N]
	
	anchor = 0
	for i in range(len(digits) - 1):
		if digits[i] < digits[i + 1]:
			anchor = i + 1
			
		if digits[i] > digits[i + 1]:	# Number is not tidy
			digits[anchor] -= 1
			for j in range(anchor + 1, len(digits)):
				digits[j] = 9
			break
	
	tidy = ''.join(str(d) for d in digits)
	tidy = int(tidy)
	
	print 'Case #%i:' % (t + 1), tidy
