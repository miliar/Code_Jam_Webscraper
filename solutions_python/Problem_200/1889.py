
result = ''

def is_tidy(num):

	c = 0

	for i in xrange( len(num) ):
		if int(num[i]) < c:
			return False
		else :
			c = int(num[i])

	return True

	pass


def check_result(num):

	global result

	if is_tidy(num):
		result = num
		return

	while '0' in num:
		
		new = ''
		for i in xrange(num.find('0'), len(num)):
			new+='0'

		num = num[0:num.find('0')] + new
		num = str( int(num) - 1 )
		# print num

	while True:
		digit_list = []
		for i in xrange(len(num)):
			digit_list.append( int(num[i]) )
		
		max_digit = 0
		for idx, i in enumerate(digit_list):
			if i >= max_digit:
				max_digit = i
			else:
				
				digit_list[idx-1] = digit_list[idx-1] - 1

				for j in xrange(idx, len(digit_list)):
					digit_list[j] = 9

				break

		num = ''
		for i in digit_list:
			num = num + str(i)

		if is_tidy(num):
			result = num
			return

	pass

if __name__ == '__main__':

	t = int(raw_input()) 
	for k in xrange(1, t + 1):
		raw = raw_input()
		# print raw

		result = raw

		check_result(result)

		print 'Case #{}: {}'.format(k, result)


