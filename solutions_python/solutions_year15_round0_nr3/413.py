import sys

Q_MULT = {  
			'1': {'1':'1',	'i':'i', 	'j':'j', 	'k':'k'	},
		    'i': {'1':'i',	'i':'-1', 	'j':'k', 	'k':'-j'},
			'j': {'1':'j',	'i':'-k',	'j':'-1',	'k':'i'	},
			'k': {'1':'k',	'i':'j',	'j':'-i',	'k':'-1'}
		 }

def read_input(input):
	f = open(input)

	num_cases = int(f.readline())
	ijk_strings = []
	x_vals = []

	for i in range(num_cases):
		l_x_line = [int(str_num) for str_num in f.readline().split(' ')]
		true_x = min(l_x_line[1], (20+l_x_line[1]%4))
		ijk_strings.append(f.readline().strip()*true_x)
	
	return (num_cases, ijk_strings)

# num_cases => int
# ijk_strings => [int]
def main(writer, num_cases, ijk_strings):

	for i in range(num_cases):

		cur_str = ijk_strings[i]

		i_index = find_letter(0, cur_str, 'i')
		j_index = find_letter(i_index, cur_str, 'j')
		k_index = find_letter(i_index+j_index, cur_str, 'k')

		correct_spelling = False
		if -1 not in [i_index, j_index, k_index]:
			ijk_index = i_index + j_index + k_index
			correct_spelling = check_rest_is_1(ijk_index, cur_str)

		result_str = 'YES' if correct_spelling else 'NO'
		writer.write_output(i, result_str)

	return

def find_letter(index, cur_str, letter):
	rest_of_str = cur_str[index:]
	current_val = ''
	for i in range(len(rest_of_str)):
		current_val = evaluate_next(current_val, rest_of_str[i])
		if letter == current_val:
			return i+1

	return -1

def check_rest_is_1(index, cur_str):
	rest_of_str = cur_str[index:]

	current_val = ''
	for char in rest_of_str:
		current_val = evaluate_next(current_val, char)

	return current_val == '1' or rest_of_str == ''

def evaluate_next(current_val, next_char):

	if current_val == '': return next_char

	is_negative = False
	if current_val[0] == '-':
		is_negative = True
		current_val = current_val[1]

	new_val = Q_MULT[current_val][next_char]

	if is_negative:
		if new_val[0] == '-':
			new_val = new_val[1]
		else:
			new_val = '-' + new_val

	return new_val

class Writer():

	def __init__(self):
		self.output = open('outputs/' + sys.argv[1].split('/')[1][:-2] + 'out', 
						   'w+')
	
	def write_output(self, iteration_num, result_str):
		result_base = "Case #"+str(iteration_num+1)+": "
		self.output.write(result_base+result_str+'\n')

if __name__ == "__main__":
	formatted_input = read_input(sys.argv[1])
	w = Writer()
	main(w, *formatted_input)
	w.output.close()


# mappings = [	
# 						{'letter': 'i', 'cur_val':'', 'next_char':''},
# 						{'letter': 'j', 'cur_val':'', 'next_char':''},
# 						{'letter': 'k', 'cur_val':'', 'next_char':''},
# 					 ]
		
# 		cur_letter = 0
# 		rest_is_1 = True
		
# 		for j in range(len(cur_str)):
# 			if cur_letter < 3:
# 				mappings[cur_letter]['next_char'] = cur_str[j]
# 				letter_built = build_next_val_and_check(mappings[cur_letter])
				
# 				if letter_built:
# 					cur_letter += 1
# 			else:
# 				rest_is_1 = check_rest_is_1(i, cur_str)
# 				break