#infile = open('/home/patanjali/Desktop/A-small-attempt0(2).in')
infile = open('/home/patanjali/Desktop/A-large.in')
#outfile = open('/home/patanjali/codejam/A-small.out','w')
outfile = open('/home/patanjali/codejam/A-large.out','w')

import sets

num_cases = int(infile.readline().strip())

for case_no in xrange(1,num_cases+1,1):
	code = infile.readline().strip()
	code_list = list(code)
	if len(sets.Set(code_list)) > 1:
		digits = [[x for x in code_list[1:] if x != code_list[0]][0], code_list[0]]
		for char in code_list[2:]:
			if char not in digits:
				digits.append(char)
		base = len(digits)
		war_is_at = 0
		for char in code_list:
			war_is_at = war_is_at*base + digits.index(char)
	else:
		war_is_at = 2**len(code_list)-1

	outfile.write("Case #%s: %s\n" %(case_no, war_is_at))

infile.close()
outfile.close()
