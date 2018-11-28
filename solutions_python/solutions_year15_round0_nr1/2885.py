#!/usr/bin/python

import fileinput


def solve(Smax, S):
	#for every i>0 the following must hold:
	#SUM(from i=1 to i=i) S_{i-1} >= if S_i != 0
	sum=0;
	min_friends=0;

	#according to the description always will be a person in the audience 
	if Smax==0: 
		return 0;

	for i in range(1,Smax+1):
		sum = sum + int(S[i-1])
		if int(S[i]) > 0:
			if sum < i:
				min_friends = min_friends + i-sum
				sum=i;

	return min_friends
			


line_cnt=0
test_cases=1

for line in fileinput.input():
	if(line_cnt > (test_cases)):
		#print 'error'
		break;
	if(line_cnt == 0):
		test_cases=int(line.rstrip());
	else:
		line=line.split();
		Smax=int(line[0]);
		S=line[1];
		friends=solve(Smax, S)
		print('Case #'+str(line_cnt)+': '+ str(friends))
	line_cnt+=1;
