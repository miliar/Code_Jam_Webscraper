def find_result(smax , other):
	p = 0;
	f = 0;
	for i in xrange(smax+1):
		if i+1 == 1:
			pass
		elif i+1 <= p:
			pass
		elif i+1 > p:
			f = f + (i-p) 
			p = p + int(other[i]) + (i-p)
			continue 

		p = p + int(other[i]) 

	return f 



test_case = input()
case = 0
fout = open('fil.txt','w')

while(case < test_case):
	string = raw_input().split()
	smax = string[0]
	other = string[1]

	fout.write( 'Case #%s: %s\n' %(case +1, find_result(int(smax) ,other) ) ) 


	case = case + 1;

