import sys
test = int(sys.stdin.readline())
for i in xrange(test):
	m, string = map(str,sys.stdin.readline().split())
	standing_person = int(string[0]);
	required_person = 0;	
	for ind,val in enumerate(string[1:]):
		if(standing_person<ind+1 and int(val)!=0):
			required_person+= ind+1-standing_person
			standing_person+= ind+1-standing_person		
		standing_person+=int(val)
	sys.stdout.write("Case #"+str(i+1)+":"+" "+str(required_person)+'\n')

