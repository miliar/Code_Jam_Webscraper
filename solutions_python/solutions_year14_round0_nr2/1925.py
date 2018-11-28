input_file = open("ex.in")
output_file = open('ex.out', 'w')
def next_line():
	return input_file.readline()
def test_farms(ammount, C, F, X):
	prod = 2
	secs = 0
	if ammount == 0:
		return X/prod
	for x in range(ammount):
		secs += C / prod
		prod = prod + F
	secs += X / prod
	return secs
cases = int(next_line())
for case_number in range(cases):
	C, F, X = next_line().split( )
	last = False
	i = 0
	while(True):
		i+=1
		new = test_farms(i, float(C), float(F), float(X))
		if last and last < new:
			output_file.write('Case #'+str(case_number+1)+': '+str(last)+'\n')
			break
		last = new