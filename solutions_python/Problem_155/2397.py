f = open('A-small-attempt1.in', 'r')
#f = open('trial.in', 'r')
content = f.read().split("\n")

no_of_cases = content[0]

case_no = 0
for line in content[1:-1]:
	case_no += 1
	case_size = int(line.split(" ")[0])
	case = line.split(" ")[1]
	case = [int(i) for i in case]
	
	if case_size == 0:
		print "Case #%d: %d" % (case_no, case_size)
		continue
	
	END_POWER_NEEDED = 0
	for level in reversed(range(len(case))):
		if level > 0:
			POWERNEEDED = max(0, level  - sum(case[:level]))
			#print 'POWERNEEDED '+ str(POWERNEEDED) +' on level '+ str(level)
		
		if POWERNEEDED > END_POWER_NEEDED: END_POWER_NEEDED = POWERNEEDED
		
	print "Case #%d: %d" % (case_no, END_POWER_NEEDED)
			
			
	
