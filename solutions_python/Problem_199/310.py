# Read file and parse

filename = "A-large"
#filename = "practice"
infile= filename + '.in'
f = open(infile)
inp = f.read().splitlines()
f.close()
outfile = filename + '.out'
f = open(outfile,'w')
case = int(inp.pop(0))

# Solve here
def Solve(line):
	S,K = line.split()
	S = list(S)
	K = int(K)
	len_S = len(S)
	count = 0;
	for i in range(0, len_S-K+1):
		while S[i] == '+' and i <= len_S-K:
			i += 1
		if i > len_S - K:
			break
		count += 1		
		for j in range(i, i+K):
			if S[j] == '-':
				S[j] = '+'
			else:
				S[j] = '-'			
	for i in range(len_S-K, len_S):
		if S[i] != '+':
			return "IMPOSSIBLE"
	return count			 	


# Output
for case in range(1, case + 1):
	result = Solve(inp[case-1])
	print('Case #{}: {}'.format(case, result))
	f.write('Case #{}: {}\n'.format(case, result))
f.close()	
