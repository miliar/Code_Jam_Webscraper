# saving the univerese
for case in range(input()):
	search_engines = []
	for n in range(input()):
		search_engines.append(raw_input())
	
	switches = 0
	search_set = set(search_engines)
	incoming_queries = []
	for n in range(input()):
		query = raw_input()
		if query in search_set:
			search_set.remove(query)
		if len(search_set) == 0:
			# switch
			switches += 1
			search_set = set(search_engines)
			search_set.remove(query)	
	
	print 'Case #%s: %s' % (case + 1, switches)
