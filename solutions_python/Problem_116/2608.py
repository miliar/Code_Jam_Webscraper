N = input()
#print "Num of test cases:", N

plan = [['.' for i in range(1,5)] for j in range(1,5)]
	
def check(k):	
	#Skontroluj stlpce
	for i in xrange(0,4):
		j = 0;
		if(plan[j][i] == '.'): continue
		else: pivot = plan[j][i]
		j+=1
		while j<4 and (plan[j][i] == pivot or plan[j][i] == 'T'):
			j+=1
		if(j == 4): 
			print "Case #%d: %s won" % (k,pivot)
			return

	#Skontroluj riadky
	for i in xrange(0,4):
		j = 0
		if(plan[i][j] == '.'): continue
		else: pivot = plan[i][j]
		j+=1
		while  j<4 and (plan[i][j] == pivot or plan[i][j] == 'T'):
			j+=1
		if(j == 4):
			print "Case #%d: %s won" % (k,pivot)
			return

	#Uhlopriecka zlava doprava
	if(plan[0][0] != '.'):
		pivot = plan[0][0]
		i = 1
		while i<4 and (plan[i][i] == pivot or plan[i][i] == 'T'):
			i+=1
		if(i == 4):
			print "Case #%d: %s won" % (k,pivot)
			return

	#Uhlopriecka zprava dolava
	if(plan[0][3] != '.'):
		pivot = plan[0][3]
		i = 1
		while i<4 and (plan[i][3-i] == pivot or plan[i][3-i] == 'T'):
			i+=1
		if(i == 4): 
			print "Case #%d: %s won" % (k,pivot)
			return

	#Skontroluj nedohranost
	for i in xrange(0,4):
		if("." in plan[i]):
			print "Case #%d: Game has not completed" % (k)
			return;

	#Remiza
	print "Case #%d: Draw" % (k)


for x in xrange(1,N+1):
	plan = [['.' for i in range(1,5)] for j in range(1,5)]
	#print "Case:",i
	for i in xrange(0,4):
		a = raw_input()
		for j in xrange(0,4):
			plan[i][j] = a[j]
	#print plan
	if (x != N): raw_input()
	check(x)
