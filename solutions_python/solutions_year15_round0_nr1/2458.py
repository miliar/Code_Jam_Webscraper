def find_result(smax , other):
	people = 0;
	friends = 0;
	for i in xrange(smax+1):
		if i+1 == 1:
			pass
		elif i+1 <= people:
			pass
		elif i+1 > people:
			friends = friends + (i-people) 
			people = people + int(other[i]) + (i-people)
			continue 

		people = people + int(other[i]) 

	return friends 



test_case = input()
cas = 0
fout = open('file.txt','w')

while(cas < test_case):
	string = raw_input().split()
	smax = string[0]
	other = string[1]

	fout.write( 'Case #%s: %s\n' %(cas+1, find_result(int(smax) ,other) ) ) 


	cas = cas + 1;

