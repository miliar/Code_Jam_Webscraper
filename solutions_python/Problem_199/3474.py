
def flip(from_n, by_k, pancake_stack):
	running = from_n
	for k in range(by_k):
		if (pancake_stack[running] == '+'):
			pancake_stack[running] = '-'
		else:
			pancake_stack[running] = '+'
		running += 1
		if running == len(pancake_stack):
			break
		

	
def get_first_unfliped(pancake_stack):
	# make it get next by reducing by the last size
	for position, letter in enumerate(pancake_stack):
		if (letter == '-'):
			return position



def run():
	input_file = open('small2017large.in', 'r')
	output_file = open('small2017large.out', 'w')
	first_line = input_file.readline() # read the first line of the content of the small.in file
	T = int(first_line) # convert the string file to integer
	for no in range(1, T+1):
		next_line = next(input_file)
		pancake_row = next_line.split(" ")[0]
		k_size = int(next_line.split(" ")[1])
		pancake_row_list = list(pancake_row)
		count = 0
		result = ""
		while( get_first_unfliped(pancake_row_list) != None):
			pos = get_first_unfliped(pancake_row_list)
			if ( pos + k_size - 1) < len(pancake_row_list):
				flip(pos, k_size, pancake_row_list)
				count += 1
			else: 
				count = -1
				break
		if count == -1:
			output_file.write('Case #{}: {}\n'.format(no, "IMPOSSIBLE"))
		else:
			output_file.write('Case #{}: {}\n'.format(no, count))

		


run()
