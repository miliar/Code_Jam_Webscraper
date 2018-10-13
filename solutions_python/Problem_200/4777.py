def tidy_number(n):
	last_digit = n % 10
	n = n / 10
	while n > 0:
		if n % 10 > last_digit:
			return False
		else:
			last_digit = n % 10
			n = n/10
	return True

if __name__ == '__main__':
	f = open('C:\Users\sdhupar\Downloads\B-small-attempt0.in')
	line_cnt = 0
	inpts = []
	test_case = 0
	for line in f:
		if line_cnt == 0:
			test_case = int(line)
			line_cnt += 1
		else:
			inpts.append(int(line.rstrip('\n')))
	
	for i in range(test_case):
		for j in range(inpts[i],-1,-1):
			if tidy_number(j):
				print "Case #"+str(i+1)+": "+str(j)
				break