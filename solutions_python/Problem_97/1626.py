from sets import Set

def compute_recycled_numbers_max(n, max):
	computed_valid_m = Set()
	for i in xrange(1, len(n)):
		m = int(n[-i:] + n[:len(n) - i])
		
		if(int(n) < m and m <= max):
			computed_valid_m.add(m)
	
	return len(computed_valid_m)

def compute_recycled_pairs_between(min, max):
	pairs = 0
	if len(str(min)) > 1:
		for n in xrange(min, max + 1):
			pairs += compute_recycled_numbers_max(str(n), max)
	
	return pairs

def main():	
	for T in xrange(int(raw_input())):
		A, B = map(int, (raw_input().split()))
		print 'Case #{0}: {1}'.format(T + 1, compute_recycled_pairs_between(A, B))

if __name__ == '__main__':
	main()

