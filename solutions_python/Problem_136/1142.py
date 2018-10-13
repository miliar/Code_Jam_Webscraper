import sys
import os

in_file = str(sys.argv[1]) 
out_file = os.path.splitext(in_file)[0] + '.out'

fin = open(in_file, 'r')
nr_of_cases = int(fin.readline())

fout = open(out_file, 'w')

cases_done = 0

def solve_case(c, f, x):
	cr = 2.0
	elapsed = 0.0
	click = 0.0
	buy = 0.0
	while True:
		click = x/cr + elapsed
		buy = c/cr + x/(cr+f) + elapsed
		if click < buy:
			return click
		else:
			elapsed += c/cr
			cr += f

while cases_done < nr_of_cases:
	cases_done += 1
	
	args = fin.readline().split()
	c = float(args[0])
	f = float(args[1])
	x = float(args[2])
	
	answer = solve_case(c, f, x)
	
	fout.write('Case #{0}: '.format(cases_done))
	fout.write('{0:.7f}'.format(answer))
	fout.write('\n')
	
fin.close()
fout.close()
