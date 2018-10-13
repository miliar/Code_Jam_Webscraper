def calc_wp(line):
	wins = 0	;lost = 0;
	for i in line:
		if(i=='0'):
			lost+=1
		elif(i=='1'):
			wins+=1
	return float(wins)/(wins+lost)
def calc_owp(nr,line,tmp_owp):
	wyn = 0;
	cnt = 0;
	for i in range(len(line)):
		if(line[i]!='.'):
			wyn+=tmp_owp[i][nr]
			cnt+=1;
	return wyn/cnt
		
def calc_oowp(nr,line,owp):
	wyn = 0;
	cnt = 0;
	for i in range(len(line)):
		if(line[i]!='.'):
			wyn+=owp[i]
			cnt+=1
	return float(wyn)/cnt
		
#	
def calc_tmp_owp(line):
	lost=0;wins=0
	for i in line:
		if(i=='0'):
			lost+=1;
		elif(i=='1'):
			wins+=1;
	sin_line = []
	for i in line:
		wyn = 0;
		if(i=='.'):
			wyn=float(wins)/(wins+lost)	
		elif(i=='0'):
			wyn=float(wins)/(wins+lost-1)
		else:#if i=='1'
			wyn=float(wins-1)/(wins-1+lost)
		sin_line.append(wyn)
	return sin_line
		
def fun():
	N = int(raw_input())
	array = []
	wp = []
	tmp_owp = []
	owp=[]
	oowp=[]
	for _ in range(N):
		array.append(list(raw_input()))
	#inp = [int(x) for x in inp.split()]
	#N = inp[0]; Pd = inp[1]; Pg = inp[2];
	for line in array:
		wp.append(calc_wp(line))
	for line in array:
		tmp_owp.append(calc_tmp_owp(line))
	for line in range(len(array)):
		owp.append(calc_owp(line,array[line],tmp_owp))
	for line in range(len(array)):
		oowp.append(calc_oowp(line,array[line],owp))
		
	for x in range(len(oowp)):
		print 0.25*wp[x]+0.5*owp[x]+0.25*oowp[x]
		


tests = int(raw_input())
t = 1
while(t<=tests):
	print "Case #%s:"%t
	fun()
	t+=1
	
	
