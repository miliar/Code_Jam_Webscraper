#!/usr/bin/python -tt

def main():
	dict = {}
	dict['a'] = 'y'
	dict['b'] = 'h'
	dict['c'] = 'e'
	dict['d'] = 's'
	dict['e'] = 'o'
	dict['f'] = 'c'
	dict['g'] = 'v'
	dict['h'] = 'x'
	dict['i'] = 'd'
	dict['j'] = 'u'
	dict['k'] = 'i'
	dict['l'] = 'g'
	dict['m'] = 'l'
	dict['n'] = 'b'
	dict['o'] = 'k'
	dict['p'] = 'r'
	dict['q'] = 'z'
	dict['r'] = 't'
	dict['s'] = 'n'
	dict['t'] = 'w'
	dict['u'] = 'j'
	dict['v'] = 'p'
	dict['w'] = 'f'
	dict['x'] = 'm'
	dict['y'] = 'a'
	dict['z'] = 'q'
	dict[' '] = ' '
	dict['\n'] = ''
	f = open('input.txt', 'rU')
	w = open('output.txt', 'w')
	lineCount=0
	lineTemp = 1
	for line in f:
		lineCount+=1
		if lineCount is 2:
			lineNumber = int(line)
			print 'LineNumber :', lineNumber
		if lineCount > 2 and (lineCount <= (2 + lineNumber)):
			w.write('Case #' + str(lineTemp) + ": ")
			for word in line:
				#print word
				w.write( dict[word],)
			w.write('\n')
			lineTemp += 1
			
	f.close()


def writeFile(string, filename):
	filename.write(string)



if __name__ == '__main__':
  main()
