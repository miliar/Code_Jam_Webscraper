import sys	


flip = {'+': '-', '-': '+'}


def last_tidy(N):
	tidy = str(N)
	if len(tidy) == 1:
		return N
	i = len(tidy) - 2
	while i > -1:
		if int(tidy[i]) > int(tidy[i + 1]):
			new_tidy = tidy[:i]
			new_tidy += str(int(tidy[i]) - 1)
			new_tidy += (len(tidy) - i - 1) * '9'
			tidy = new_tidy
		i -= 1
	return int(tidy)		

def solve_case(case, f, fout):
	N = int(f.readline().strip())
	result = last_tidy(N)
	write_line(fout, case, str(result))

def write_line(fout, n, result):
	print("Case #%d: %s\n" %(n, result))
	fout.write("Case #%d: %s\n" %(n, result))

if __name__ == '__main__':
	
	input_file_name = sys.argv[1]
	
	f = file(input_file_name)
	fout = file("%s.out" %(input_file_name.split(".")[0]), "w")
	
	T = eval(f.readline())
	
	for case in xrange(T):
		solve_case(case + 1, f, fout)
		
	f.close()
	fout.close()
