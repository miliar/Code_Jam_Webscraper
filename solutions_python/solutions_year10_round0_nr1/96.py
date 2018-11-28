"""
Snapper Chain
"""
import sys

def Solve(n,k):
	mod = 2 ** n 
	if (k % mod == mod - 1):
		return 'ON'
	else:
		return 'OFF'

if __name__ == "__main__":
	input_file = open(sys.argv[1])
	output_file = open(sys.argv[2],'w')
	t = int(input_file.readline())
	for i in range(t):
		ss = input_file.readline()
		li = ss.split(' ')
		res = Solve(int(li[0]),int(li[1]))
		output_file.write('Case #' + str(i+1) + ': ' + res + '\n')

	input_file.close()
	output_file.close()
		

