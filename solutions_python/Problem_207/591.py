
rules = {'R': ['R'], 'O': ['R', 'Y'], 'G': ['Y', 'B'], 'V': ['R', 'B'], 'Y': ['Y'], 'B': ['B']}

def main():
	for case in xrange(int(raw_input())):
		inp = map(int, raw_input().split())
		n = inp[0]
		amounts = dict(zip('R O Y G B V'.split(), inp[1 : ]))
		#For small data set only !!
		m = max(amounts.values())
		s = sum(amounts.values()) - m
		ans = 'IMPOSSIBLE'
		if m <= s:
			sep = max(amounts.keys(), key = lambda k: amounts[k])
			amount = amounts.pop(sep)
			ans = [''] * m
			count = 0
			for a in amounts:
				for i in xrange(amounts[a]):
					ans[count % m] = a + ans[count % m]
					count += 1
			ans = ''.join([a + sep for a in ans])
		print 'Case #{}: {}'.format(case + 1, ans)

if __name__ == '__main__':
	main()