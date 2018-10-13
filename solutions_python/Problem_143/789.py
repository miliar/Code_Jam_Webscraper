def p2(A, B, K):
	ans = 0
	for i in xrange(A):
		for j in xrange(B):
			if ((i & j) < K):
				ans += 1 
	return ans

def read_input():
	input_file = open('input1.in', 'rb')
	lines = input_file.readlines()
	input_file.close()

	num_input = int(lines[0])
	lines = lines[1:]
	t = 1
	output_file = open('p2_result.txt','wb')
	for l in lines:
		A, B, K =  [int(i) for i in l.strip().split()]
		output_file.write('Case #'+str(t)+': '+ str(p2 (A, B, K))+'\n')
		t = t + 1

	output_file.close()


def main():
	read_input()



if __name__ == '__main__':
	main()