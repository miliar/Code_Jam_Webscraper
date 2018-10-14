

char_dictionary = {
					'a':'y',
					'b':'h',
					'c':'e',
					'd':'s',
					'e':'o',
					'f':'c',
					'g':'v',
					'h':'x',
					'i':'d',
					'j':'u',
					'k':'i',
					'l':'g',
					'm':'l',
					'n':'b',
					'o':'k',
					'p':'r',
					'q':'z',
					'r':'t',
					's':'n',
					't':'w',
					'u':'j',
					'v':'p',
					'w':'f',
					'x':'m',
					'y':'a',
					'z':'q',
					' ':' ',
					'\n':'\n'}
					
					
def convert(line):
	ans = ''
	for el in line:
		ans += char_dictionary[el]
	else:
		return ans
		
		
if __name__ == '__main__':
	input_file = open('A-small-attempt9.in')
	submit_file = open('out', 'w')
	for (number, line) in enumerate(input_file):
		if number == 0:
			continue
			
		submit_file.write('Case #{}: '.format(number) + convert(line))
		
	else:
		submit_file.close()
		

