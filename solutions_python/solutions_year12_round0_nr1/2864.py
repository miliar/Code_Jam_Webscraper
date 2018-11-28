import sys

def self():
	time_taken_O = 0;
	time_taken_B = 0;
	position_O = 1;
	position_B = 1;
	time = 0
	push = 1

	filename = 'test.in'
	if len(sys.argv)==2:
		filename = sys.argv[1]
	out = filename[:-3]+'.out'
	print out
	f = open(filename)
	w = open(out, 'w')
	tests = int(f.readline())

	i = 0
	while i < tests:
		print i
		i = i+1
		line = f.readline()
		print line
		j = 0
		trans = ''
		
		while j < len(line):
			if(  line[j] =='a'):
				trans+='y';
			elif(line[j] =='b'):
				trans+='h';
			elif(line[j] =='c'):
				trans+='e';
			elif(line[j] =='d'):
				trans+='s';
			elif(line[j] =='e'):
				trans+='o';
			elif(line[j] =='f'):
				trans+='c';
			elif(line[j] =='g'):
				trans+='v';
			elif(line[j] =='h'):
				trans+='x';
			elif(line[j] =='i'):
				trans+='d';
			elif(line[j] =='j'):
				trans+='u';
			elif(line[j] =='k'):
				trans+='i';
			elif(line[j] =='l'):
				trans+='g';
			elif(line[j] =='m'):
				trans+='l';
			elif(line[j] =='n'):
				trans+='b';
			elif(line[j] =='o'):
				trans+='k';
			elif(line[j] =='p'):
				trans+='r';
			elif(line[j] =='q'):
				trans+='z';
			elif(line[j] =='r'):
				trans+='t';
			elif(line[j] =='s'):
				trans+='n';
			elif(line[j] =='t'):
				trans+='w';
			elif(line[j] =='u'):
				trans+='j';
			elif(line[j] =='v'):
				trans+='p';
			elif(line[j] =='w'):
				trans+='f';
			elif(line[j] =='x'):
				trans+='m';
			elif(line[j] =='y'):
				trans+='a';
			elif(line[j] =='z'):
				trans+='q';
			elif(line[j] ==' '):
				trans+=' ';
			print trans
			j=j+1
		w.write('Case #'+str(i)+': '+trans+'\n')


if __name__ == "__main__":
	self()
