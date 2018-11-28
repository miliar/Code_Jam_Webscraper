import sys

input_list = []
output_list = []

def get_result(input_list):
	C = input_list[0]
	F = input_list[1]
	X = input_list[2]
	if X <= C:
		return X/2.0
	return T(C, F, X)

# after buying n farm, velocity
def A(C, F, X, n):
	return 2.0+(F*n)
	
def B_n_fx(C, F, X, n, B_n_1):
	return B_n_1+(C/A(C, F, X, n-1))

def T(C, F, X):
	n = 0
	T_n = X/2.0
	B_n = 0
	T_n_prev = X/2.0
	while T_n_prev >= T_n:
		n += 1
		T_n_prev = T_n
		B_n = B_n_fx(C, F, X, n, B_n)
		T_n = B_n + (X/A(C, F, X, n))
		#print T_n_prev, T_n
	return T_n_prev
	
try:
	input_filename = sys.argv[1]
	output_filename = input_filename[:sys.argv[1].find('.')]+'.out'
except:
	print 'input filename as argv'
	exit()

try:
	input_f = open("./"+input_filename)
	input_lines = input_f.readlines()
	input_lines2 = []
	input_lines2_count = 0
	i = 0
	j = 0
	for i in range(1, len(input_lines)):
		input_line = input_lines[i]
		input_line_split = input_line.split()
		input_line_split_float = map(float, input_line_split)
		input_list.append(input_line_split_float)
	input_f.close()
	
	#print input_lines2

except:
	print 'read error'
	exit()

#input_list.pop(0)

for x in input_list:
	# do some works here
	print x
	result = get_result(x)
	output_list.append([result])
	print

try:
	output_f = open("./"+output_filename, "w")
	output_f.close()
except:
	pass

try:
	output_f = open("./"+output_filename, "a")
	output_str = ''

	for x in range(len(output_list)):
		output_f.write('Case #' + str(x+1)+': '+str(output_list[x][0])+"\n")
		print x
	output_f.close()
except:
	print 'write error'
	exit()
