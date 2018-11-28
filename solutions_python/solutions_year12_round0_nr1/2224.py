def run():
	tp = 'yhesocvxduiglbkrztnwjpfmaq'
	fin = open('a.in', 'r')
	n = fin.readline()
	fout = open('a.out', 'w')
	c = 1
	for line in fin:
		s = ""
		for j in range(len(line)):
			if line[j] == ' ':
				s += ' '
			else:
				if ord(line[j])-ord('a') >= 0:
					s += tp[ord(line[j])-ord('a')]
		fout.write('Case #%d: %s\n'%(c, s))
		c += 1

if __name__ == '__main__':
	run()
