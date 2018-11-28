import sys
def main():
	fin=open(sys.argv[1],'r');
	fout=open(sys.argv[2],'w')
	num_lines=int(fin.readline())
	for i in range(num_lines):
		instr=fin.readline()
		outstr="Case #"+str(i+1)+": "
		for letter in instr:
			if letter == 'a':
				outstr+='y'
			elif letter == 'b':
				outstr+='h'
			elif letter == 'c':
				outstr+='e'
			elif letter == 'd':
				outstr+='s'
			elif letter == 'e':
				outstr+='o'
			elif letter == 'f':
				outstr+='c'
			elif letter == 'g':
				outstr+='v'
			elif letter == 'h':
				outstr+='x'
			elif letter == 'i':
				outstr+='d'
			elif letter == 'j':
				outstr+='u'
			elif letter == 'k':
				outstr+='i'
			elif letter == 'l':
				outstr+='g'
			elif letter == 'm':
				outstr+='l'
			elif letter == 'n':
				outstr+='b'
			elif letter == 'o':
				outstr+='k'
			elif letter == 'p':
				outstr+='r'
			elif letter == 'q':
				outstr+='z'
			elif letter == 'r':
				outstr+='t'
			elif letter == 's':
				outstr+='n'
			elif letter == 't':
				outstr+='w'
			elif letter == 'u':
				outstr+='j'
			elif letter == 'v':
				outstr+='p'
			elif letter == 'w':
				outstr+='f'
			elif letter == 'x':
				outstr+='m'
			elif letter == 'y':
				outstr+='a'
			elif letter == 'z':
				outstr+='q'
			else:
				outstr+=letter
		print outstr
		fout.write(outstr)
	fin.close()
	fout.close()


if __name__=="__main__":
	main()
