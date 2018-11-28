#!/usr/bin/python 

import sys 
import Queue 

def process(line1, line2):	
	last = 0
	sumc = 0

	price = 0
	
	R = int(line1[0])
	K = int(line1[1])
	N = int(line1[2])

	q = Queue.Queue()
		
	for i in range(N):
		q.put(int(line2[i]))
	#print R
	for i in range(R):
		q1 = Queue.Queue()
		while(sumc + last <=K):
			q1.put(last)
			#print sumc, last
			sumc += last
			price += last 
			if(q.empty()):
				last = 0
				break
			
			last = q.get()
		
		#print "-----"+ str(sumc) + "____" + str(price) + "---" + str(last)
		
		while(not q1.empty()):
			q.put(q1.get())
			
		
		sumc = 0
		
			
	return(price)
					
				
				
				
				
				
		
	
	

	
		
	

		
	

if(__name__=="__main__"):
	nTestCases = int(sys.stdin.readline().strip())

	for i in range(1,nTestCases+1):
                inputs = sys.stdin.readline().strip().split(" ")
		inputs1 = sys.stdin.readline().strip().split(" ")
		string = "Case #" + str(i) + ": "
                print string + str(process(inputs, inputs1))
		#break
		
			
	
	
	
