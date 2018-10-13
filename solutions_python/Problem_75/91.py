def combine(rules, e1, e2):
	for rule in rules:
		b1, b2, nb = rule
		if e1 == b1 and e2 == b2:
			return nb
		elif e1 == b2 and e2 == b1:
			return nb
	return None

def oppose(rules, base):
	for rule in rules:
		b1, b2 = rule
		if b1 in base and b2 in base:
			return []		
	return base
		
f = open('B-large.in', 'r')

T = int(f.readline()[:-1])
for case_no in range(1, T + 1):
	case  = f.readline()[:-1].split(' ')
	C = int(case[0])
	D = int(case[C + 1])
	N = int(case[C + D + 2])
	combine_rules = case[1:C + 1]
	oppose_rules = case[C + 2: C + D + 2]
	base = [char for char in case[-1]]
	elements = []
	for i in range(0, len(base)):
		elements.append(base[i])
		if C > 0 and len(elements) > 1:
			e = combine(combine_rules, elements[-1], elements[-2])
			if e is not None:
				elements = elements[:len(elements) - 2]
				elements.append(e)
		if D > 0:
			elements = oppose(oppose_rules, elements)
	if len(elements) > 0:
		result = ''.join(elements[0])
	else:
		result = ''
	for i in range(1, len(elements)):
		result = result + ', ' + elements[i]
	print "Case #%s: [%s]" % (case_no, result)

