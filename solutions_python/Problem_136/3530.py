#B: Cookie clicker alpha
'''
count time to get to n farms.
if time to get to n-1 farms then to the end is less,
this time is the answer
increase values of n from 0 until this occurs
'''



prob_file = open('B-small-attempt0.in', 'r')#open the file containing the problems

out_file = open('out_b.txt', 'w')

lines = []
for line in prob_file:
		lines.append(line)
		
num_cases = lines[0]

lines_per = 1

def time_for_farms(num_farms):
	time = 0
	rate = 2
	
	num_made = 0
	while num_made < num_farms:
		time += farm_cost / rate
		rate += farm_add
		num_made += 1
		
	time += target_num / rate
	return time

for i in range(1, len(lines)):
		case_line = lines[i]
		case_values = case_line.split()

		farm_cost = float(case_values[0])
		farm_add = float(case_values[1])
		target_num = float(case_values[2])
		rate = 2
				
		num_farms = 0
		while time_for_farms(num_farms) > time_for_farms(num_farms+1):
			num_farms += 1
		time = time_for_farms(num_farms)
					 
		
		case_num = 'Case #'+str(i)
		case_return = case_num + ': ' + str(time)
		out_file.write(case_return+'\n')
		
