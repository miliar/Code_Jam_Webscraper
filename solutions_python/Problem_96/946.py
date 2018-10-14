testcase = None
while not testcase:
    try:
        testcase = int(raw_input())
    except ValueError:
        print 'Invalid testcase'

for i in range(testcase):
	s = raw_input();
	s_list = s.split(' ');
	googlers = int(s_list[0]);
	srp = int(s_list[1]);
	max_score = int(s_list[2]);
	clearvalid= 0
	survalid = 0
	for j in range(googlers):
		score = int(s_list[j+3]);
		rest_score = score-max_score;
		if rest_score >=0:
			if rest_score%2 == 0:
				second_score = rest_score/2;
			else:
				second_score = (rest_score-1)/2;
			third_score = score-(second_score+max_score);
		
			firstdiff = abs(max_score-second_score);
			seconddiff = abs(max_score-third_score);
		
			if firstdiff>=seconddiff:
				diff = firstdiff;
			else:
				diff = seconddiff;
		
			if diff==1 or diff ==0:
				clearvalid = clearvalid+1
			elif max_score<second_score or max_score<third_score:
				clearvalid = clearvalid+1
			elif diff==2:
				survalid = survalid+1
		if survalid > srp:
			survalid = srp
	print 'Case #'+str(i+1)+': '+str(clearvalid+survalid)
		
			
		
		
	