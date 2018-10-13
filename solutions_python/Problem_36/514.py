from sys import stdin

def num_welcomed(string, search):
	if search == '':
		return 1
	elif string == '':
		return 0
	else:
		n = 0
		for (i, c) in enumerate(string):
			if c == search[0]:
				n += num_welcomed(string[i + 1:], search[1:])		
		return n

n = int(stdin.readline()[:-1])
for x in range(1, n + 1):
	print('Case #%d: %s' % (x, str(num_welcomed(stdin.readline()[:-1], 'welcome to code jam'))[-4:].zfill(4)))
