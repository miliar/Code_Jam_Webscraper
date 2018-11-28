from collections import defaultdict

def test_cases():
	from sys import stdin
	
	stdin.readline()
	for line in stdin:
		yield line.strip().split(' ')

def parse_case_data(case_data):
	replacements = {}
	oppositions = defaultdict(list)
	
	for _ in xrange(int(case_data.pop(0))):
		repl = case_data.pop(0)
		replacements[(repl[0], repl[1])] = repl[2]
		replacements[(repl[1], repl[0])] = repl[2]
	
	for _ in xrange(int(case_data.pop(0))):
		opp = case_data.pop(0)
		oppositions[opp[0]].append(opp[1])
		oppositions[opp[1]].append(opp[0])
	
	invocations = case_data.pop(1)
	return (replacements, oppositions, invocations)

for (case_number, case_data) in enumerate(test_cases()):
	replacements, oppositions, invocations = parse_case_data(case_data)
	elements = []
	element_counts = defaultdict(lambda: 0)

	for invocation in invocations:
		elements.append(invocation)
		element_counts[invocation] += 1

		if len(elements) > 1:
			last_pair = tuple(elements[-2:])
			if last_pair in replacements:
				repl = replacements[last_pair]
				elements[-2:] = (repl, )
				element_counts[last_pair[0]] -= 1
				element_counts[last_pair[1]] -= 1
				element_counts[repl] += 1

			for opp in oppositions.get(elements[-1], []):
				if element_counts[opp] > 0:
					elements = []
					element_counts.clear()
					break
					
	
	print "Case #%d: [%s]" % (case_number+1, ', '.join(elements))