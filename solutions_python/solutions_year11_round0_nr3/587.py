def test_cases():
	from sys import stdin
	
	cases = int(stdin.readline())
	for i in xrange(cases):
		stdin.readline()
		yield map(int, stdin.readline().strip().split(' '))

def partitions(all_data):
	from itertools import combinations
	for i in xrange(1,len(all_data)/2+1):
		for set1 in combinations(all_data, i):
			set2 = list(all_data)
			for i in set1:
				set2.remove(i)
			yield (set1, set2)

for (case_number, case_data) in enumerate(test_cases()):
	xorer = lambda a,b: a^b
	max_partition_sum = None
	
	for (set1, set2) in partitions(case_data):
		if reduce(xorer, set1) == reduce(xorer, set2):
			partition_sum = max(sum(set1), sum(set2))
			if partition_sum > max_partition_sum:
				max_partition_sum = partition_sum

	print "Case #%d: %s" % (case_number+1, max_partition_sum or 'NO')
