def main():
	for TEST in xrange(1, int(raw_input())+1):
		answer1 = int(raw_input())
		grid1 = [map(int, raw_input().split()) for _ in xrange(4)]
		answer2 = int(raw_input())
		grid2 = [map(int, raw_input().split()) for _ in xrange(4)]

		possible = set(grid1[answer1-1]).intersection(set(grid2[answer2-1]))
		size = len(possible)

		if size == 1:
			print "Case #%d: %d" % (TEST, list(possible)[0])
		elif size == 0:
			print "Case #%d: %s" % (TEST, "Volunteer cheated!")
		else:
			print "Case #%d: %s" % (TEST, "Bad magician!")

main()
