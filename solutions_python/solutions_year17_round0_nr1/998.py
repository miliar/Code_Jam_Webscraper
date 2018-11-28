def solve(s, k):
	s = [1 if c == '+' else 0 for c in s]
	l = len(s)
	num = 0
	for i in range(0, l-k+1):
		if s[i] == 0:
			num += 1
			for f in range(i, i+k):
				s[f] = 1-s[f]
	res = True
	for i in range(l-k+1, l):
		if s[i] == 0:
			res = False
			break
	if res:
		return num
	else:
		return 'IMPOSSIBLE'


def getInput():
	n = int(input())
	inputs = []
	for i in range(0, n):
		line = input()
		l = line.split(' ')
		inputs.append((l[0], int(l[1])))
	return n, inputs
	
def getInputFromFile(filename):
	f = open(filename, 'rt')
	n = int(f.readline().rstrip())
	inputs = []
	for i in range(0, n):
		line = f.readline().rstrip()
		l = line.split(' ')
		inputs.append((l[0], int(l[1])))
	f.close()
	return n, inputs	
	
	
def getAns(filename):
	n, inputs = getInputFromFile(filename)
	res = []
	for i in range(0, n):
		ans = solve(inputs[i][0], inputs[i][1])
		res.append('Case #{}: {}'.format(i+1, ans))
	f = open('pancake_output.txt', 'wt')
	s = '\n'.join(res)
	print(s)
	f.write(s)
	f.close()


