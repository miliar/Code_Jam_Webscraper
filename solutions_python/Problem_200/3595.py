
def check_tidy(num):
	s = str(num)
	retVal = True
	if len(s) > 0:
		for i in range(1,len(s)):
			prev = s[i-1]
			curr = s[i]
			
			if int(curr) < int (prev):
				retVal = False
				break;
	return retVal
					
def check_large_tidy(num):
	s = str(num)
	st= s
	n = len(s)
	pos = n-1
	retVal = num
	if check_tidy(num):
		retVal = num
		return retVal
	else:
		while(pos >= 1):
			
			new_s = list(st)
			if int(new_s[pos]) == 9:
				pos = pos-1
			else:
				new_s[pos] = '9'
				pos = pos - 1
				while(new_s[pos] == '0'):
					new_s[pos] = '9'
					pos = pos-1
				e = str(int(new_s[pos]) -1)
				new_s[pos] = e
			st = ''.join(new_s)
			if check_tidy(int(st)):
				retVal = int(st)
				return retVal
			
## for small
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
	n = int(raw_input())
	ans = check_large_tidy(n)
	print "Case #{}: {}".format(i, ans)

