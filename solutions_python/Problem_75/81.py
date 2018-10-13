from itertools import groupby

for T in range(int(raw_input())):
	data = raw_input().split(' ')
		
	combine = dict((s[:2], s[2]) for s in data[1 : 1 + int(data[0])] + [r[1] + r[0] + r[2] for r in data[1 : 1 + int(data[0])]]) 
	oposed = dict()
	for k in (s for s in data[2 + int(data[0]) : -2] + [r[::-1] for r in data[2 + int(data[0]) : -2]]):
		oposed.setdefault(k[0], []).append(k[1])
	invoke = data[-1]
	
	element_list = list()
	for spell in invoke:
		if element_list and (element_list[-1] + spell) in combine:
			element_list[-1] = combine[element_list[-1] + spell]
		else:
			element_list.append(spell)
		
		if element_list[-1] in oposed:
			for op in oposed[element_list[-1]]:
				if op in element_list:
					element_list = list()
					break
	
	print 'Case #%d: [%s]' % (T + 1, ', '.join(element_list))

