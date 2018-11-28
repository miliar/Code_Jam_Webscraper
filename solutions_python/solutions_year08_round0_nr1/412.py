
def main():
	case_n = int(raw_input())
	for case_loop in range(0, case_n):
		se = {}
		rq = []
		se_n = int(raw_input())
		for se_loop in  range(0, se_n):
			se[raw_input()] = 0
		rq_n = int(raw_input())
		for rq_loop in range(0, rq_n):
			rq.append(raw_input())
		print "Case #%s: %s" % (case_loop + 1, schedule(se, rq))
		#print se
		#print rq
		
def fill_zero(se):
	for key in se.keys():
		se[key] = 0
	return se

def schedule(se, rq):
	def zero_use((iter, val)): 
		return val == 0
	switch = 0
	for request in rq:
		least_use = filter(zero_use, se.iteritems())
		#print se
		#print "#", least_use
		if len(least_use) == 1:
			least_use_name, v = least_use[0]
			#print least_use_name, request
			if least_use_name == request:
				switch += 1
				for key in se.keys():
					se[key] = 0
		se[request] += 1

				
	if switch == -1:
		switch = 0
	return switch
			
			

main()
