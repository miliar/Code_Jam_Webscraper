def solve(case, line):
	
	elements =line.split(' ')
	num_elements = int(elements[0])+1
	vanitystr = elements[1]
	added = 0
	standed = 0
	for standing_needed in range(0,num_elements):
		additional = 0
		# print 'case: %s standed: %s standing_needed:%s ' % (case, standed, standing_needed)
		if standed >= standing_needed:
			standed = standed + int(vanitystr[standing_needed])
		else:
			additional = standing_needed - standed
			added = added + additional
			standed = standed + additional
			standed = standed + int(vanitystr[standing_needed])
	return 'Case #%s: %s\n' % (case, added)


inputname='A-large.in'
file = open(inputname, 'r')
writefile = open('output.txt','w')
count =0
for line in file:
	count=count+1
	if count>1:
		outputline = solve(count-1, line)
		writefile.write(outputline)

