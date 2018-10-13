import sys
size = raw_input()
a = []
for line in sys.stdin:
	a.append(int(line))

def printCase(iteration, N):
	out = "Case #" + str(iteration) + ": "
	
	N_str = str(N)
	if len(N_str) == 1:
		print out + N_str
		return
		
	left_digit = N_str[0]
	last_tidy = ""
	same_since = 0
	for i in xrange(1, len(N_str)):
		right_digit = N_str[i]
		if (int(left_digit) > int(right_digit)):
			if (same_since != i):
				last_tidy = N_str[0:same_since]
				last_tidy += str(int(left_digit) - 1)
				last_tidy += ("9"*(len(N_str) - same_since - 1))
				break
			last_tidy += str(int(left_digit) - 1)
			last_tidy += ("9"*(len(N_str) - i))
			break
		else:
			same_since = same_since if right_digit == left_digit else i
			last_tidy += left_digit
			if (i == len(N_str) -1 ):
				last_tidy += right_digit
			left_digit = right_digit

	
	print out + str(int(last_tidy))
		


for i in xrange(len(a)):
	printCase(i+1, a[i])