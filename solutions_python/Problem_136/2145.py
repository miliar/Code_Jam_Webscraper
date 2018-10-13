from __future__ import division


R=2
IN_FILE_NAME = 'test.in'
OUT_FILE_NAME = 'test.out'

def solve(X,F,C,R):
	total_time = 0
	time_left_not_buying = X/R
	time_left_buying = C/R + X/(R+F)

	while time_left_buying < time_left_not_buying:
		total_time += C/R
		R += F	
		time_left_not_buying = X/R
		time_left_buying = C/R + X/(R+F)

	total_time += X/R
	return total_time

def main():
	in_file = open(IN_FILE_NAME,'r')
	out_file = open(OUT_FILE_NAME,'w')
	number_of_cases = in_file.readline()
	for case in range(1,int(number_of_cases)+1):
		data = in_file.readline().split(' ')

		C=float(data[0])
		F=float(data[1])
		X=float(data[2])
		
		result = solve(X,F,C,R)
		to_write = 'Case #'+str(case)+': '+str(result)+'\n'
		out_file.write(to_write)
main()



