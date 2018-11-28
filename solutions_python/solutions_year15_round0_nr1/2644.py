def main():
	for TEST in xrange(1, int(raw_input())+1):
		_, people_str = raw_input().split()
		people = map(int, people_str)

		count = 0
		extras = 0

		for i,p in enumerate(people):
			if i > count:
				extras += i-count
				count += i-count
			count += p

		print "Case #%d: %s" % (TEST, str(extras))

main()
