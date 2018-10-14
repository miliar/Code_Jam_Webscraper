letter_mapping = {
		'a': 'y', 
		'b': 'h', 
		'c': 'e', 
		'd': 's', 
		'e': 'o', 
		'f': 'c',
		'g': 'v',
		'h': 'x',
		'i': 'd',
		'j': 'u',
		'k': 'i',
		'l': 'g',
		'm': 'l',
		'n': 'b',
		'o': 'k',
		'p': 'r',
		'q': 'z',
		'r': 't',
		's': 'n',
		't': 'w',
		'u': 'j',
		'v': 'p',
		'w': 'f',
		'x': 'm',
		'y': 'a',
		'z': 'q',
		' ': ' ',
		'\n': '\n'}

def translate(string):
	translated = ''
	for char in string:
		translated += letter_mapping[char]
	return translated

def setup_from_args():
	import sys
	if len(sys.argv) == 1:
		print("Use 'python googlereze.py input_file [output_file]'")
		quit()
	elif len(sys.argv) == 2:
		output_file = 'googlereze_output.txt'
	else:
		output_file = sys.argv[2]
	input_file = sys.argv[1]

	input_ = open(input_file, 'r')
	output = open(output_file, 'w')
	return input_, output

if __name__ == '__main__':
	
	input_, output = setup_from_args()

	T = int(input_.readline())

	G_list = []
	for __ in range(T):
		G_list.append(input_.readline())

	for i, G in enumerate(G_list):
		output.write('Case #' + str(i + 1) + ': ' + translate(G))
