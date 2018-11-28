#!/usr/bin/env python

def input():
	n_cases=int(raw_input())
	result=[]
	for i in range(n_cases):
		s_engines=int(raw_input())
		engines=[]
		for j in range(s_engines):
			temp=raw_input()
			engines.append(temp)
		q_queries=int(raw_input())
		queries=[]
		for j in range(q_queries):
			temp=raw_input()
			queries.append(temp)

		result.append(calculateSwitches(i,engines,queries))
	for i in range(len(result)):
		print "Case #%d: %d" % (i+1,result[i])


def calculateSwitches(case_number,engines, queries):
	"""print "Case #%d: 2" % (case_number)
	for i in engines:
		print i
	print "----------------------------"
	for i in queries:
		print i"""

	if(len(queries)==0):
		return 0;	
	dup=[]
	siz=len(queries)
	temp=""
	for i in queries:
		if(temp!=i):
			dup.append(i)
			temp=i
	table=[[-1]*len(engines)]*len(queries)
	min=0

	for i in range(len(engines)):
		if(engines[i]==queries[0]):
			table[0][i]=-1
		else:
			table[0][i]=min

	for i in range(1,len(queries)):
		flag=0
		for j in range(len(engines)):
			if(queries[i]==engines[j]):
				table[i][j]=-1
			else:
				table[i][j]=table[i-1][j]
				if(table[i][j]!=-1):
					flag=1
		if(flag==0):
			min=min+1
			for j in range(len(engines)):
				if(queries[i]==engines[j]):
					table[i][j]=-1
				else:
					table[i][j]=min
	
	return min;
	
					
		
	
	


input()	
