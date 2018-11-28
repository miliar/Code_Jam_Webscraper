import sys

input_list = []
output_list = []

try:
	input_filename = sys.argv[1]
	output_filename = input_filename[:sys.argv[1].find('.')]+'.out'
except:
	print 'input filename as argv'
	exit()

try:
	input_f = open("./"+input_filename)
	input_lines = input_f.readlines()
	input_count = 0
	for input_line in input_lines:
		input_split = input_line.split()
		input_list.append(map(int, input_split))
		# input_list.append(input_line.strip())
	input_f.close()
except:
	print 'read error'
	exit()

input_list.pop(0)

def get_arr(K, C, S):
	if S<K:
		return 'IMPOSSIBLE'
	result_arr = []
	for i in range(K):
		result_arr.append(i+1)
	for i in range(1, C):
		for j in range(K):
			result_arr[j] = (result_arr[j]-1) * K + j + 1
	return ' '.join(map(str, result_arr))

for input_item in input_list:

	# do some works here
	print input_item
	result = get_arr(input_item[0], input_item[1], input_item[2])
	#result += ''
	output_list.append([result])

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
