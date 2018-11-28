from sys import argv, setrecursionlimit
from os.path import expanduser


# Import the file as a list of lines:
problem = argv[1]
path = expanduser('~/Downloads/')
file_in = path + problem + '.in'
file_out = path + problem + '.out.txt'

setrecursionlimit(2000)
def A(stalls,k):
	max_gap = max(stalls)
	max_index = stalls.index(max_gap)
	if max_gap%2 == 0:
		insert = [max_gap/2-1,max_gap/2]
	else:
		insert = [max_gap/2,max_gap/2]
	newstalls = stalls[:max_index] + insert + stalls[max_index+1:]
	k -= 1
	if k == 0:
		return insert[::-1]
	else:
		return A(newstalls,k)



with open(file_in,'rb') as fin, open(file_out,'wb') as fout:
	
	lines = fin.read().splitlines()
	case = 1

	for l in lines[1:]:
		ls = l.split()
		n = [int(ls[0])]
		k = int(ls[1])
		
		answer = A(n,k)

		output = 'Case #%d: %s %s\n' % (case,answer[0],answer[1])
		fout.write(output)
		case += 1
