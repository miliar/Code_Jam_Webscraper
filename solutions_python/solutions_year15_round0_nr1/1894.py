import fileinput
f = fileinput.input()

def stand(inpstr):
	inp = inpstr.split()
	n = int(inp[0]) + 1
	str = inp[1]
	x = 0
	cnt = 0
	for i in xrange(n):
		s = int(str[i])
		if x < i and s > 0:
			cnt += i - x
			x += cnt
			
		x += s
	
	return cnt

def read_input():
	t = int(f.readline())
	input_str = []
	for i in xrange(t):
		input_str.append(f.readline())
		
	case = 1
	for input in input_str:
		res = stand(input)
		output = "Case #"+str(case)+": "+str(res)
		print output
		case += 1
	

read_input()
