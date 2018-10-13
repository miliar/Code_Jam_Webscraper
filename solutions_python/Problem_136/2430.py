def calc_solution(lines):
	solutions = []
	no_cases = long(lines[0])

	index = 1
	for case in range(0,no_cases):
		(C,F,X) = [float(v) for v in lines[index].split()]
		index += 1

		no_cookies = 0.0
		rate = 2.0
		time = 0.0
		while no_cookies < X:
			if no_cookies >= C:
				# Decide whether we should buy the farm.
				expected_time_no_farm = (X-no_cookies)/rate
				expected_time_farm = (X-(no_cookies-C))/(rate+F)
				if expected_time_farm <= expected_time_no_farm:
					rate += F
					no_cookies -= C
				else:
					# If not, progress to X
					time += (X-no_cookies)/rate
					no_cookies = X
			else:
				# Progress to the next time we can buy
				# a farm, or have X cookies
				next_amount = min(C,X)
				time += (next_amount-no_cookies)/rate
				no_cookies = next_amount

		solutions.append(time)

	return solutions


#########################################################

fin_name = 'B-large.in'
fout_name = 'solution-B-large'

fin = open(fin_name,'r')
lines = [string.split("\n")[0] for string in fin.readlines()]

solutions = calc_solution(lines)

fout = open(fout_name,'w')
for i,solution in enumerate(solutions):
	fout.write("Case #%s: %s\n" % (i+1,solution))