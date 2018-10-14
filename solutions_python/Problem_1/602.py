
def remove_largest(queries, engines):
	#now we have the engines and queries
	#determine the frequency of each engine
	engine_freq = {}
	max_queries = 0
	max_worker = None
	for engine1 in engines.values():
		for engine2 in queries:
			if engine1 != engine2:
				if engine1 in engine_freq:
					engine_freq[engine1].append(engine2)
				else:
					engine_freq[engine1] = [engine2]
			else:
				if engine1 in engine_freq:
					break
				else:
					engine_freq[engine1] = []
					break
		if len(engine_freq[engine1]) > max_queries:
			max_queries = len(engine_freq[engine1])
			max_worker = engine1

	if len(engine_freq) != len(engines):
		#then we can use an engine to search all queries
		return []
	else:
		#the best place to start is max_worker 
		for query in engine_freq[max_worker]:
			queries.remove(query)
		return queries

input = open('c:\\large_input_saving_universe.in', 'r')
output = open('c:\\large_output_saving_universe.txt', 'w')
tests = int(input.readline())

for test in range(tests):
	num_engines = int(input.readline().strip())
	engines = {}
	for i in range(num_engines):
		engines[i] = input.readline().strip()
	num_queries = int(input.readline().strip())
	
	queries = []
	for i in range(num_queries):
		queries.append(input.readline().strip())

	if len(queries) == 0:
		output.write('Case #' + str(test+1) + ': ' + str(0) + '\n')
	else:
		switches = -1
		while len(queries) > 0:
			queries = remove_largest(queries, engines)
			switches += 1
		output.write('Case #' + str(test+1) + ': ' + str(switches) + '\n')

output.close()
input.close()
		
	
	
	
	

					
		
			


