import itertools

def equal_sum_subsets(s):
	for length1 in xrange(1, len(s)/2 + 1):
		for s1 in itertools.combinations(s, length1):
			for length2 in xrange(length1, len(s)):
				for s2 in itertools.combinations(s, length2):
					if(sum(s2) > sum(s1)): break
					if(sum(s1) == sum(s2) and s1 != s2):
						print ' '.join(map(str, s1))
						print ' '.join(map(str, s2))
						return
	
	print 'Impossible'
	

def main():	
	for T in xrange(int(raw_input())):
		print 'Case #{0}:'.format(T + 1)
		equal_sum_subsets(sorted(map(int, raw_input().split()[1:])))

if __name__ == '__main__':
	main()