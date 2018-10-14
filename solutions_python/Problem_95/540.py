translation_dict = {
	'y': 'a',
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
	'q': 'z'
}

def int_input():
	return int(raw_input());

def solve():
	line = raw_input();
	translated_line = '';
	for char in line:
		if translation_dict.has_key(char):
			translated_char = translation_dict[char];
		else:
			translated_char = char;
		translated_line += translated_char;
	return translated_line;

def main():
	for i in range(1, int_input()+1):
		print 'Case #%d: %s' % (i, solve());

main();