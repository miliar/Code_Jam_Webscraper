import sys

def readFile(filename):
	L = []
	with open(filename, 'r') as fp:
		T = int(fp.readline())
		for i in range(T):
			L.append(fp.readline().strip())
	return T, L	

def solve(S):
	if len(S) == 1:
		return S[0]
	S = [int(s) for s in S]
	n = len(S)
	while True:
		flag = False
		for i in range(n-1):
			if S[i] > S[i+1]:
				flag = True
				break;
		if flag:
			S[i] = S[i]-1
			if S[i] < 0:
				S[i] = 9
			for j in range(i+1, n):
				S[j] = 9
		else:
			break
	output = ''.join([str(s) for s in S])
	i = 0
	while i < len(S) and output[i] == '0':
		i += 1
	output = output[i:]
	return output

if __name__ == "__main__":
	input_filename = sys.argv[1]
	T, L = readFile(input_filename)
	output_fp = open('output.txt', 'w')
	for i in range(T):
		result = "Case #{}: {}".format(i+1, solve(L[i]))
		output_fp.write(result)
		if not i==T-1:
			output_fp.write('\n')
	
