import re
#from itertools import islice, count
#islice(count(start,step),(stop-start+step-1+2*(step<0)))
T = int(raw_input())
for t in range(T):
	n = long(raw_input())
	num = n
	#series = xrange(1,n+1)
	#numbers = xrange(1,n+1)[::-1]
	tidy = None
	while num > 0:
		string_num = str(num)
		string_digit_list = re.findall('\d',string_num)
		digit_list = map(int,string_digit_list)
		if ( sorted(digit_list) == digit_list):
			tidy = num
			break
		num = num - 1
	print ('Case #'+ str(t+1)+': '+str(tidy))