def main():
	n = int(raw_input())
	for num in range(n):

		s = int(raw_input())
		names = []
		for x in range(s):
			names.append(raw_input())

		q = int(raw_input())
		queries = []
		for x in range(q):
			queries.append(raw_input())

		queries.reverse()

		switches = 0
		possible = set(names)
		for q in queries:
			if q in possible:
				possible.remove(q)
				if not possible:
					switches += 1
					possible = set(names)
					possible.remove(q)

		print "Case #%d: %d" % (num + 1, switches)

main()
