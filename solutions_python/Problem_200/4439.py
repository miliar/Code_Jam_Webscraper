
def is_tidy_number(num):
	index = len(num) - 1
	num = list(num)
	while index:
		#compare index and index - 1
		if num[index] < num[index - 1]:
			return 0
		index = index - 1	
	return 1
	
	
#num is string
def tidy_numbers(num):
	flag = 1
	index = 0
	length = len(num)
	num = list(num)
	while index != length - 1:
		#compare index and index - 1
		if num[index] > num[index + 1]:
			#first time decrement index
			num[index] = str(int(num[index]) - 1)
			num[index + 1] = '9'
			break		
		index = index + 1
	while index != length - 1:
		num[index + 1] = '9'
		index = index + 1	
		
	#delete leading zeros	
	if num[0] == '0':
		num = num[1:]	
	#convert it to string	
	num = ''.join(num)		
	return num			



n = input()

for i in range(n):
	num = raw_input()
	out = tidy_numbers(num)
	while(not is_tidy_number(out)):
		out = tidy_numbers(out)
	print "Case #" + str(i+1) + ": " + out
	
