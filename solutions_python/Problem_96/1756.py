#Javier Fernandez Google Code Jam 2012
# javierfdr@gmail.com - javierfdr
# Google Dance

import sys

def parse_file(in_file):
	num_cases = int(in_file.readline())
	cases_list = []
	for c in range(num_cases):
		case = in_file.readline().strip("\n").split()
		cases_list.append(case)
		
	return cases_list

# returns the number of scores over p given the score list and the 
# surprise attempts allowed
def get_max_p(score_list, s, p):
	over_count = 0
	for score in score_list:
		common_score = score/3
		rest_score = score%3
	
		assumed_surprise = False
	
		# assuming a substraction and add to a score, condition to surprise
		if(rest_score==0 and score>=2):
			rest_score = 1
			assumed_surprise = True
		
		# overpassed - easy
		if(common_score >= p):
			over_count+=1
			continue
		
		if(rest_score >0):
			if(common_score+1 >= p):
				over_count +=1
				
				if(assumed_surprise and s==0):
					over_count-=1
				
				if(assumed_surprise and s>0):
					s-=1
					assumed_surprise = False
				
				#if(not assumed_surprise):
				#	print 'thanks to +1'
				
				continue
			if(rest_score >1):
				if(((common_score+2) >= p) and (s >0)):
					s-=1
					over_count+=1
					continue
	return over_count

out_file = open('output.out','w+')
in_file = sys.stdin
case_list = parse_file(in_file)
count = 1
for case in case_list :
	n = int(case[0])
	s = int(case[1])
	p = int(case[2])
	scores = []
	for c in range(3,3+n):
		scores.append(int(case[c]))

	over_count = get_max_p(scores,s,p)
	out_file.write("Case #"+str(count)+": "+str(over_count)+'\n')
	count+=1

#for c in range(1,num_cases+1):
#	case = 'Case #'+str(c)+': '
#	result= case+ str(size_of_loop(blue_list[c-1],red_list[c-1]))+'\n'
#	out_file.write(result)

