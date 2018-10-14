
def check_tidy(n):
	digits = [int(d) for d in str(n)]
	return sorted(digits) == digits

t = int(raw_input())

# for each test case
for i in range(t):
	N = raw_input()

	# small cases
	if len(N) <= 3:
		N = int(N)
		while(check_tidy(N) == False):
			N -= 1
		print("Case #"+str(i+1)+": " + str(N))

	# large cases
	else:
		digits = [int(d) for d in N]
		
		one_less = False
		flip = 0
		for n in range (1, len(digits)):

			if (digits[n-1] < digits[n]):
				flip = n

			elif (digits[n-1] > digits[n]):
				
				# flip digit down
				digits[flip] = digits[flip] - 1
				if (digits[flip]==0):
					digits[flip] = 9
					one_less = True

				# turn all the rest 9
				for j in range(flip+1, len(digits)):
					digits[j] = 9

		dig_char = map(str, digits)
		dig_str = ''.join(dig_char)     
		if one_less:
			print("Case #"+str(i+1)+": " + dig_str[:-1])
		else:
			print("Case #"+str(i+1)+": " + dig_str)


			
		



