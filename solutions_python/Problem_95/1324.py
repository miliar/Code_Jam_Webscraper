#!/usr/bin/python

my_dict = {
	' ' : ' ',
	'\n' : '\n',
	'a' : 'y',
	'b' : 'h',
	'c' : 'e' ,
	'd' : 's',
	'e' : 'o',
	'f' : 'c',
	'g' : 'v',
	'h' : 'x',
	'i' : 'd',
	'j' : 'u',
	'k' : 'i',
	'l' : 'g',
	'm' : 'l',
	'n' : 'b',
	'o' : 'k',
	'p' : 'r',
	'q' : 'z',
	'r' : 't',
	's' : 'n',
	't' : 'w',
	'u' : 'j',
	'v' : 'p',
	'w' : 'f',
	'x' : 'm',
	'y' : 'a',
	'z' : 'q',
	}
def main ():
	char_dict = {}
	fout = open('out.txt', 'w')
	c = 1
	with open('A-small-attempt1.in', 'r') as fin:
		count = int(fin.readline())
		for line in fin:
			lineout = []
			for i in line:
				j = my_dict[i]
				lineout.append(j)
			lineout = ''.join(lineout)
			fout.write('Case #%s: %s' %( c, lineout))
			c += 1
	fout.close()

if __name__ == '__main__':
	main ()

				
