import sys

def dictionary(x):
	if x=='a': return 'y'
	elif x=='b':return 'h'
	elif x=='c':return 'e'
	elif x=='d':return 's'
	elif x=='e':return 'o'
	elif x=='f':return 'c'
	elif x=='g':return 'v'
	elif x=='h':return 'x'
	elif x=='i':return 'd'
	elif x=='j':return 'u'
	elif x=='k':return 'i'
	elif x=='l':return 'g'
	elif x=='m':return 'l'
	elif x=='n':return 'b'
	elif x=='o':return 'k'
	elif x=='p':return 'r'
	elif x=='q':return 'z'
	elif x=='r':return 't'
	elif x=='s':return 'n'
	elif x=='t':return 'w'
	elif x=='u':return 'j'
	elif x=='v':return 'p'
	elif x=='w':return 'f'
	elif x=='x':return 'm'
	elif x=='y':return 'a'
	elif x=='z':return 'q'
	elif x==' ':return ' '


if __name__ == "__main__":

	f=sys.stdin
	f=sys.argv[1]
	myfile=open(f)
	T=int(myfile.readline())
	for i in range(T):
		line=list(myfile.readline())
		for j in range(len(line)):
			line[j]=dictionary(line[j])
		print "Case #"+str(i+1)+": "+''.join(line[:len(line)-1])
			
