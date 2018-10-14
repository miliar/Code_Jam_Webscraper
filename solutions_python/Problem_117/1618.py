

def checker(N, M, lawn):
	def check_lawn(lawn, max_list):
		for r in range(N):
			for c in range(M):
				patch = lawn[r*M+c]
				if patch < max_list[r]:
					if patch < max_list[N+c]:
						return 'NO'
		return 'YES'

	#N+M max element in row/column list; 
	#max of n^th row is max_list[n]
	#max of m^th col is max_list[N+m]
	max_list = []
	#finds maximum element in each row
	maximum = 0	
	for r in range(N):
		for c in range(M):
			maximum = max(maximum, lawn[r*M+c])
		max_list.append(maximum)
		maximum = 0
	#finds maximum element in each column
	for c in range(M):
		for r in range(N):
			maximum = max(maximum, lawn[r*M+c])
		max_list.append(maximum)
		maximum = 0
	#print N, M, lawn, max_list
	return check_lawn(lawn, max_list)
	

input_file = open('small_input', 'r')
output_file = open('small_output', 'w')
#input_file = open('large_input', 'r')
#output_file = open('large_output', 'w')
num_lawns = int(input_file.readline())
output = ''

for i in range(1, num_lawns+1):
	dimensions = input_file.readline().split()
	N, M = int(dimensions[0]), int(dimensions[1])
	#print N, M
	lawn = '\n'
	lawn_digital = []
	for j in range(N):
		new_row = input_file.readline()
		lawn += new_row
		lawn_digital.extend( new_row.split() )
	#print 'lawn #{0} is: \n{1}'.format(i, lawn)
	#print 'lawn_digital #{0} is: \n{1}'.format(i, lawn_digital)
	output += 'Case #{0}: {1}\n'.format(i, checker(N, M, lawn_digital))
output_file.write(output)

output_file.close()
input_file.close()