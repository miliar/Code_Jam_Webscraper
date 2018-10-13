
def solve(data):
	C, D, N = data
	invoke = []
	table = {}

	for s in C:
		table[s[0] + s[1]] = s[2]
		table[s[1] + s[0]] = s[2]
	for c in N:
		invoke.append(c)
		if len(invoke) > 1:
			s = ''.join(invoke[-2:])
			if s in table:
				invoke = invoke[:-2] + [table[s]]
		for s in D:
			if s[0] in invoke and s[1] in invoke:
				invoke = []

	return '[%s]' % (', '.join(invoke))

def get_input():
	tmp = raw_input().split()
	C = int(tmp[0])
	D = int(tmp[C + 1])
	N = int(tmp[C + D + 2])
	return tmp[1:C+1], tmp[C+2:C+D+2], tmp[C+D+3]

def main():
	T = int(raw_input())
	for i in xrange(T):
		print 'Case #%s: %s' % (i + 1, solve(get_input()))

if __name__ == '__main__':
	main()
