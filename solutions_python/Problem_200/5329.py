t=int(raw_input())

def check_tidy(num):
	string = str(num)
	string = list(string)
	
	if(string == sorted(string)):
		return True
	else:
		return False

for i in range(t):
	line = int(raw_input())
	while (not check_tidy(line)) and line>0:
		line-= 1
	print "Case #%i: %i" % (i+1,line)

	