
input = []
with open("C-small-attempt0.in") as f:
	for line in f:
		input.append(line)
		
		
cases = input[1:]

number_of_cases = int(input[0])

output = open('output.out', 'w')

for case in range(number_of_cases):
		
	

	runs_in_day = int(cases[2*case].split()[0]) #R
	seats = int(cases[2*case].split()[1]) #k
	# unnecessary variable:  number of groups = #N

	string_groups = cases[(2*case)+1]

	groups = []

	for sub in string_groups.split():
		groups.append(int(sub))
		
	# that parses

	day_total = 0


	for run_number in range(runs_in_day):
		people_sat = 0
		groups_sat = 0
		for group in groups:
			if ((people_sat + group) > seats):
				break
			else:
				people_sat += group
				groups_sat += 1
		day_total += people_sat
		sat_groups = groups[:groups_sat]
		groups = groups[groups_sat:] + sat_groups
		#groups = groups[groups_sat:].append(groups[0:groups_sat])
		
	print 'Case #{0}: {1}'.format(case + 1, day_total)
	output.write('Case #{0}: {1}\n'.format(case + 1, day_total))
