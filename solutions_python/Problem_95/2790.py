



if __name__ == '__main__':

	code = \
	{' ': ' ',
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
	 'z': 'q'}

	with open('A-small-attempt1.in','r') as inp:
		input_data = inp.readlines()
		input_data = input_data[1:]
		outarray=[]
		for idx,i in enumerate(input_data):
			i = i.strip()
			output = "Case #%d: "%(idx+1)
			for char in i:
				output+=code[char]
			output+='\n'
			outarray.append(output)
		with open('a.out','w') as out:
			out.writelines(outarray)

