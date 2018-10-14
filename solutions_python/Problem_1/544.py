def do():
	sEngs = []
	queries = []

	s = input()
	for i in range(s):
		x = raw_input();
		sEngs.append(x)

	q = input()
	for i in range(q):
		x = raw_input();
		queries.append(x)

	ret = 0
	dict = {}
	for e in sEngs:
		dict[e] = False

	for q in queries:
		dict[q] = True

		# If all are true.. increment
		for k, v in dict.iteritems():
			if not v:
				break
		else:
		 	ret += 1
			for e in sEngs:
				dict[e] = False
			dict[q] = True
#		print dict
	
	return ret

def main():
	n = input()
	for i in range(n):
		numSwitches = do()
		print 'Case #' + str(i+1) + ':', numSwitches

main()
