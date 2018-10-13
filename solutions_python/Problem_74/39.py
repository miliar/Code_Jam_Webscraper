import sys

data = sys.stdin.readlines()
tests = int(data[0])

def solve(s):
	total = 0
	b_pos = o_pos = 1
	b_reserve = o_reserve = 0
	s = s.split()[1:]
	while s != []:
		player = s[0]
		button = int(s[1])
		s = s[2:]
		if player == 'B':
			time = max(0,abs(button-b_pos)-b_reserve)+1
			total = total+time
			b_pos = button
			b_reserve = 0
			o_reserve = o_reserve+time
		else:
			time = max(0,abs(button-o_pos)-o_reserve)+1
			total = total+time
			o_pos = button
			o_reserve = 0
			b_reserve = b_reserve+time
	return total
	

for i in range(1,tests+1):
	result = solve(data[i])
	print "Case #%d: %d"%(i,result)
