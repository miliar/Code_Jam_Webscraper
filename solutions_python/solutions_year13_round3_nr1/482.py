def main():
	consonants = set("bcdfghjklmnpqrstvwxyz")

	for TEST in xrange(1, int(raw_input())+1):
		line = raw_input().split()
		string, n = line[0], int(line[1])
		L = len(string)

		indexes = []

		for i in xrange(L-n+1):
			for k in xrange(n):
				if string[i+k] not in consonants:
					break
			else:
				indexes.append(i)

		lastInd = -1
		n_values = 0
		for ind in indexes:
			n_values += (ind-lastInd) * (L-ind-n+1)
			lastInd = ind

		print "Case #%d: %s" % (TEST, str(n_values))

main()
