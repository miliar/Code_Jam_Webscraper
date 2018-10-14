
def clean(digits):
	if len(digits) < 2:
		return digits
	while digits[0] == 0:
		del digits[0]
	return digits

if __name__ == '__main__':
	t = int(input()) 
	for case_num in range(1, t + 1):
		n = int(input())
		digits = [int(c) for c in str(n)]
		
		# remove all leading 0s
		digits = clean(digits)
		
		if len(digits) == 1:
			output = digits[0]
		else:	
			for i in range(0, len(digits) - 1):
				j = i + 1
				while j < len(digits) and digits[i] == digits[j]:
						j += 1
						
				if j < len(digits) and digits[i] > digits[j]:
					digits[i] -= 1
					digits[i+1:] = [9]*(len(digits)-i-1)
					break
			
			output = int(''.join(map(str,clean(digits))))
	
		print("Case #{}: {}".format(case_num, output))
	exit(0)