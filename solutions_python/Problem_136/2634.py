#!/usr/bin/python

import fileinput


def solve(C, F, X):
	#print C, F, X
	time=0
	farms=0
	while True:
		without_buying=X/(2.0 + farms*F)
		#print 'without_buying', without_buying
		for_farm=C/(2.0 + farms*F)
		rest=X/(2.0+(farms+1)*F)
		#print 'for farm', for_farm
		#print 'rest', rest
		with_buying=for_farm+rest
		#print 'with_buying', with_buying
		if(with_buying < without_buying):
			time+=for_farm
			#print 'buy it\'s better now you need:', time, 'secs'
		else:
			time+=without_buying
			#print 'better don\'t buy now you need:', time, 'secs'
			return time
		farms+=1;


line_cnt=0
test_cases=1

for line in fileinput.input():
	if(line_cnt > (test_cases)):
		#print 'error'
		break;
	#print line.split()
	if(line_cnt == 0):
		test_cases=int(line.rstrip());
	else:
		line=line.split();
		C=float(line[0]);
		F=float(line[1]);
		X=float(line[2]);
		time=solve(C, F, X)
		print('Case #'+str(line_cnt)+': '+'{0:.7f}'.format(time))
	line_cnt+=1;
