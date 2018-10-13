from sys import stdin, stdout
cin=open("in")
cout=open("out","w")
debug=True
n_cases=int(cin.readline().rstrip())
for case_i in xrange(1,n_cases+1):
	#Read input
	if debug:
		print case_i
	switches=0
	n_engines=int(cin.readline().rstrip())
	engines=dict([(cin.readline().rstrip(), False) for i in xrange(n_engines)])#Stores whether we have seen this.
	n_queries=int(cin.readline().rstrip())
	used=0
	
	for i in xrange(n_queries):
		query=cin.readline().rstrip()
		#If this is the name of an engine we have not already seen since the last switch
		if query in engines and engines[query]==False:
			#Mark as seen.
			engines[query]=True
			used+=1
			if debug:
				print query, "matched. Used now ", used
			#If we have seen everything, then we have to swap.
			if used==n_engines:
				#Set
				switches+=1
				#Set query to be only thing we have seen.
				used=1
				for k in engines.keys():
					engines[k]=False
				engines[query]=True
	cout.write("Case #"+str(case_i)+": "+str(switches)+"\n")
				
	
	
