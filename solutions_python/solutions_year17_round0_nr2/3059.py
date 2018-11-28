


def last_tidy_number(N):
	s = str(N)
	# list of characters in string
	L = list(s)
	numDigits = len(L)

	i = 0
	while i<numDigits-1 and L[i] <= L[i+1]:
		i += 1
	# if our index is at last digit
	if i == numDigits-1:
		return N
	while i > 0 and L[i-1] == L[i]:
		i -= 1

	L[i] = chr(ord(L[i])-1)
	for i in range(i+1, numDigits):
		L[i] = '9'
	reS = ''.join(L)
	return int(reS)



T = int(raw_input())  # read a line with a single integer
for i in xrange(1, T + 1):
  N = int(raw_input())
  print "Case #{}: {}".format(i, last_tidy_number(N))