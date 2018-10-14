

import sys
import math


def solve(line):
	line=line.split()[1:]
	
	po=1
	pb=1
	prev_o=0
	prev_b=0
	ans=0
		
	i=0
	while i<len(line):
		
		np=int(line[i+1])
		if line[i]=='O':
			da_dodje=abs(po-np)
			
			if prev_o+da_dodje<=ans:
				da_dodje=0
			else:
				da_dodje=prev_o+da_dodje-ans
			
			ans+=da_dodje+1
			prev_o=ans			
			po=np			
		else:
			da_dodje=abs(pb-np)
			
			if prev_b+da_dodje<=ans:
				da_dodje=0
			else:
				da_dodje=prev_b+da_dodje-ans
			
			ans+=da_dodje+1
			prev_b=ans						
			pb=np
		i+=2
		#print ans
	return ans


if __name__=='__main__':
	
	tcases=input()
	
	for tcase in xrange(1,tcases+1):
		line=sys.stdin.readline()
		print 'Case #%d: %d'%(tcase,solve(line))




