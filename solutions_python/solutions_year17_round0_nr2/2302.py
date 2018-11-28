





def tidy(number):
	if len(number) == 1:
		return number
	i = 2
	while i < len(number)+1:
		if number[-(i-1)] < number[-i]:
			number = str(int(number) - (int(number[-(i-1):]) + 1))
		i += 1
	return number



with open('input', 'r') as f_in:
	next(f_in)
	with open('output', 'w') as f_out:
		count = 1
		for line in f_in:
			f_out.write('Case #{}: {}\n'.format(count, tidy(line.strip())))
			count += 1