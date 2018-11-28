# Read file and parse

filename = "B-large"
infile= filename + '.in'
f = open(infile)
inp = f.read().splitlines()
f.close()
outfile = filename + '.out'
f = open(outfile,'w')
case = int(inp.pop(0))

# Solve here
def Solve(num):
	l = list(num)
	len_num = len(num)
	if len_num == 1:
		return num
	begin = 0
	for i in range(len_num-1):
		if l[i] > l[i+1]:
			i = -1
			break;
		elif l[i] < l[i+1]:
			begin = i+1
	if i == len_num-2:
		return num		
	l[begin] = str(int(l[begin])-1)
	for i in range(begin+1, len_num):
		l[i] = '9'
	s = int(''.join(l))
	return s			

		

# Output
for case in range(1, case + 1):
	result = Solve(inp[case-1])
	print('Case #{}: {}'.format(case, result))
	f.write('Case #{}: {}\n'.format(case, result))
f.close()	
