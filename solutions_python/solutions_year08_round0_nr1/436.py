#!/usr/bin/python

def get_minswitchengineindex(query_i,queries,sengine):
	if len(queries) == 0 :
		return 0
	engine_score = [ 0 for i in xrange(len(sengine)) ]
	#for engine_i in xrange(0,len(sengine)):
	#	for query_eval_i in xrange(query_i,len(queries)):
	#		if sengine[ engine_i ] == queries[ query_eval_i ] :
	#			engine_score[ engine_i ] = engine_score[ engine_i ] + 1

	for engine_i in xrange(0,len(sengine)):
		dist = 0
		for query_eval_i in xrange(query_i,len(queries)):
			if sengine[ engine_i ] == queries[ query_eval_i ]: break
			dist =  dist + 1
		engine_score[ engine_i ] = dist

	#print "score: " , engine_score
	
	maxindex = 0
	#check max
	for i in xrange(1,len(sengine)):
		if engine_score[ i ] > engine_score[ maxindex ]:
			maxindex = i
	return maxindex
	# check the min 

	#minindex = -1
	#minval = -1
	#for i in xrange(len(sengine)):
	#	if minindex == -1 and sengine[i] != queries[ query_i ]:
	#		minindex = i
	#	else:
	#		if sengine[i] != queries[ query_i ] and engine_score[i] < engine_score[minindex]:
	#			minindex = i	
	#print minindex
	#return minindex


n_cases = int(raw_input(""))


for ncase in range(0,n_cases):
	#print "-CASE START-"
	n_sengine = int(raw_input(""))
	sengine = [] 
	queries = []
	for sengine_i in xrange(0,n_sengine):
		sengine_name = raw_input("")
		sengine.append(sengine_name)
	n_query = int(raw_input(""))
	for query_i in xrange(0,n_query):
		query_name = raw_input("")
		queries.append(query_name)
	#print "Engine:" , sengine
	# - done reading input now to the calculation 

	n_switch = 0
	cur_sengine_index = 0
	cur_sengine_index = get_minswitchengineindex(0,queries,sengine)
	for query_i in xrange(0,len(queries)):
#		print "q:" , query_i
		#print "process: " , queries[query_i]
		if queries[query_i] != sengine[cur_sengine_index]:
			continue
			# yipee!
		else:
			#damn i need to switch
			n_switch = n_switch + 1
			cur_sengine_index = get_minswitchengineindex(query_i,queries,sengine)
			if queries[query_i] == sengine[cur_sengine_index]:
#				print "wrong implementation"
				break
			else: 
				continue
	# -- show the result
	print ("Case #%d: %d") % ( ncase+1 , n_switch)
