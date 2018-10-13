import copy

def transl(words):
	translated=[[]]*len(words);
	for j in range(len(words)):
		temp=list(words[j])
		for l in range(len(words[j])):
			if temp[l]=='a':
				temp[l]='y';
			elif temp[l]=='b':
				temp[l]='h';
			elif temp[l]=='c':
				temp[l]='e';
			elif temp[l]=='d':
				temp[l]='s';
			elif temp[l]=='e':
				temp[l]='o';
			elif temp[l]=='f':
				temp[l]='c';
			elif temp[l]=='g':
				temp[l]='v';
			elif temp[l]=='h':
				temp[l]='x';
			elif temp[l]=='i':
				temp[l]='d';
			elif temp[l]=='j':
				temp[l]='u';
			elif temp[l]=='k':
				temp[l]='i';
			elif temp[l]=='l':
				temp[l]='g';
			elif temp[l]=='m':
				temp[l]='l';
			elif temp[l]=='n':
				temp[l]='b';
			elif temp[l]=='o':
				temp[l]='k';
			elif temp[l]=='p':
				temp[l]='r';
			elif temp[l]=='q':
				temp[l]='z';
			elif temp[l]=='r':
				temp[l]='t';
			elif temp[l]=='s':
				temp[l]='n';
			elif temp[l]=='t':
				temp[l]='w';
			elif temp[l]=='u':
				temp[l]='j';
			elif temp[l]=='v':
				temp[l]='p';
			elif temp[l]=='w':
				temp[l]='f';
			elif temp[l]=='x':
				temp[l]='m';
			elif temp[l]=='y':
				temp[l]='a';
			else:
				temp[l]='q';	
		translated[j]=copy.deepcopy(temp);
		translated[j]=''.join(translated[j]);
	return translated;
	
			
			
			


def main():

	lines=input();
	for i in range(lines):
		state=raw_input();
		words=state.split();
		final=transl(words);
		print 'Case #%d: %s' % ((i+1), ' '.join(final));
		
	return 0;


main()
