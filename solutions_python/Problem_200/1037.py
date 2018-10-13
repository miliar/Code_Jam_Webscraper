def solve(s):
	if s == '0':
		return '0'

	s = [int(c) for c in s]
	l = len(s)
	start = 0
	end = 0
	for i in range(1, l):
		if s[i] > s[start]:
			start = i
			end = i
		elif s[i] == s[start]:
			end = i
		else:
			break
	if end != l-1:
		s[start] = s[start] - 1
		for i in range(start + 1, l):
			s[i] = 9
	return ''.join([str(c) for c in s]).lstrip('0')
		
			
	
def getInputFromFile(filename):
	f = open(filename, 'rt')
	n = int(f.readline().rstrip())
	inputs = []
	for i in range(0, n):
		line = f.readline().rstrip()
		inputs.append(line)
	f.close()
	return n, inputs	
	
	
def getAns(filename, outputFile):
	n, inputs = getInputFromFile(filename)
	res = []
	for i in range(0, n):
		ans = solve(inputs[i])
		res.append('Case #{}: {}'.format(i+1, ans))
	f = open(outputFile, 'wt')
	s = '\n'.join(res)
	print(s)
	f.write(s)
	f.close()
