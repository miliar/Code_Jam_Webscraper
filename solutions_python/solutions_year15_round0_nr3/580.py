import sys
import random
import copy

input_path = sys.argv[0].replace('.py', '') + '.in'
output_path = sys.argv[0].replace('.py','') + '.out'

op_table = [['1', 'i', 'j', 'k', '-1', '-i', '-j', '-k'],\
		 ['i', '-1', 'k', '-j', '-i', '1', '-k', 'j'],\
		 ['j', '-k', '-1', 'i', '-j', 'k', '1', '-i'],\
		 ['k', 'j', '-i', '-1', '-k', '-j', 'i', '1'],\
		 ['-1', '-i', '-j', '-k', '1', 'i', 'j', 'k'],\
		 ['-i', '1', '-k', 'j', 'i', '-1', 'k', '-j'],\
		 ['-j', 'k', '1', '-i', 'j', '-k', '-1', 'i'],\
		 ['-k', '-j', 'i', '1', 'k', 'j', '-i', '-1']]
item_table = {'1':0,'i':1,'j':2,'k':3,'-1':4, '-i':5,'-j':6,'-k':7}

def make_problem(num):
	result = []

	str_i = ['i', 'jk', 'kkkj', 'iikj', 'iijjjk', 'kkiijjkkiikj']
	str_j = ['j', 'ki', 'kkik', 'iiik', 'iijjki', 'jjiiki']
	str_k = ['k', 'ij', 'kkji', 'iiji', 'iijjkkji', 'jjiiij']
	result = str_i[random.randint(0, len(str_i)-1)] \
		 + str_j[random.randint(0, len(str_j)-1)] \
		 + str_k[random.randint(0, len(str_k)-1)]
	print result
	return result
def read_data2(input):
	problem = make_problem(100)
	return 9, problem


def calc(a, b):
	# print a,b, op_table[item_table[a]][item_table[b]]
	return op_table[item_table[a]][item_table[b]]


def read_data(input):
	line = input.readline().strip()
	data_repeat = int(line.split()[1])
	data_str = input.readline().strip()

	return data_repeat, data_str

def find_solution(data):
	data_repeat = data[0]
	data_str = data[1]

	if len(data_str) * data_repeat < 3:
		return 'NO'

	tmp = data_str[0]
	for idx in range(1, len(data_str)):
		tmp = calc(tmp, data_str[idx])

	result = ''
	if tmp == '1' :
		result = '1'
	elif tmp == '-1' :
		if data_repeat%2 == 0:
			result = '1'
		else:
			result = '-1'
	else:
		if data_repeat%2 == 0:
			if data_repeat%4 == 0:
				result = '1'
			else:
				result = '-1'
		else:
			if data_repeat == 1:
				result = tmp
			elif data_repeat+1%4 == 0:
				result = tmp
			else:
				if len(tmp) == 1:
					result = '-' + tmp
				else:
					result = tmp[1]
	
	if result == '-1':
		return 'YES'
	else:
		return 'NO'
	

def find_idx(sym, data_str):
	result = []
	if len(data_str) == 0:
		return result
	tmp = data_str[0]
	if tmp == sym:
		result.append(0)
	if len(data_str) == 1:
		return result
	for idx in range(1,len(data_str)):
		tmp = calc(tmp, data_str[idx])
		if tmp == sym:
			result.append(idx)
	return result

def find_value(sym, data_str):
	if len(data_str) == 0:
		return False
	if len(data_str) == 1:
		if data_str[0] == sym:
			return True	
	tmp = data_str[0]
	for idx in range(1,len(data_str)):
		tmp = calc(tmp, data_str[idx])
	if tmp == sym:
		return True
	return False


def find_solution_brute(data):
	if find_solution(copy.deepcopy(data)) == 'NO':
		return 'NO'
	data_repeat = data[0]
	data_str = data[1]
	new_str = ''
	for idx in range(data_repeat):
		new_str += data_str

	if len(new_str) < 3 or len(new_str) == 3 and new_str != 'ijk':
		return 'NO'


	i_idx_list = find_idx('i', new_str)
	print i_idx_list
	for i_idx in i_idx_list:
		print 'i' , new_str[0:i_idx+1]
		j_idx_list = find_idx('j', new_str[i_idx+1:])

		for j_idx in j_idx_list:
			print 'j' , new_str[i_idx+1:i_idx+1+j_idx+1]
			k_ok = find_value('k', new_str[i_idx+1+j_idx+1:])
			if k_ok == True:
				print 'k', new_str[i_idx+1+j_idx+1:]
				return 'YES'
	return 'NO'




if __name__ == '__main__':
	input_stream = open(input_path, 'r')
	output_stream = open(output_path, 'w')
	
	T = int(input_stream.readline().strip())
	for caseN in range(1, T+1):
		result = find_solution_brute(read_data(input_stream))
		out_line = 'Case #%i: %s\n' % (caseN, result)
		print out_line
		output_stream.write(out_line)


	input_stream.close()
	output_stream.close()


