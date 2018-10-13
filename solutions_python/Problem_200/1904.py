# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(t):
	# n, m = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
	n = int(input())
	s = str(n)

	wrong_pos = -1
	for pos in range(len(s) - 1): 
		if int(s[pos]) > int(s[pos+1]):
			wrong_pos = pos
			break
	
	if wrong_pos < 0:
		print("Case #{}: {}".format(i + 1, s))
		continue
	
	reverse = s[::-1]
	corrected = ''
	wrong_pos = len(reverse) - wrong_pos - 1
	wrong_pos_val = int(reverse[wrong_pos])
	#print("input: %s - wp: %d - wpv %d" % (s, wrong_pos, wrong_pos_val))
	decrement = False
	for pos in range(len(reverse)): 
		if pos < wrong_pos: 
			corrected += '9'
		elif int(reverse[pos]) == wrong_pos_val and not pos == len(reverse) - 1 and int(reverse[pos]) == int(reverse[pos + 1]): 
			corrected += '9'
		elif not decrement: 
			corrected += str(int(reverse[pos]) - 1)
			decrement = True
		else: 
			corrected += reverse[pos]
		#print("pos %d - corrected %s - reverse[pos] %s" % (pos, corrected, reverse[pos]))
	print("Case #{}: {}".format(i+1, str(int(corrected[::-1]))))

 