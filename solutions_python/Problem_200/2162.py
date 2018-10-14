from sys import argv
from os.path import expanduser

# Import the file as a list of lines:
problem = argv[1]
path = expanduser('~/Downloads/')
file_in = path + problem + '.in'
file_out = path + problem + '.out.txt'


def A(n):
	alist = list(str(n))
	x = len(alist)
	last = 0
	index = 99
	for i, d in enumerate(alist):
		if d < last:
			index = i 
			break
		last = d
	if index == 99:
		return n
	else:
		q = 10**(x-index)
		newn = (n / q) * q - 1
		return A(newn)
	

with open(file_in,'rb') as fin, open(file_out,'wb') as fout:
	
	lines = fin.read().splitlines()
	case = 1

	for l in lines[1:]:
		answer = A(int(l))

		output = 'Case #%d: %s\n' % (case,answer)
		fout.write(output)
		case += 1
