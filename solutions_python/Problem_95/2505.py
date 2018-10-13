class Googlerese:
	def __init__(self):
		#generate dictionary
		self.table = {'y': 'a', 
			'n': 'b', 
			'f': 'c',
			'i': 'd',
			'c': 'e',
			'w': 'f',
			'l': 'g',
			'b': 'h',
			'k': 'i',
			'u': 'j',
			'o': 'k', 
			'm': 'l',
			'x': 'm',
			's': 'n',
			'e': 'o', 
			'v': 'p',
			'z': 'q',
			'p': 'r',
			'd': 's',
			'r': 't', 
			'j': 'u', 
			'g': 'v',
			't': 'w',
			'h': 'x',
			'a': 'y',
			'q': 'z',
			' ': ' ',
			'\n': '\n'}

	def get_letter(self, into):
		return self.table[into]

