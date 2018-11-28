def solve(cards_row1, cards_row2):
	intersection = filter(lambda x: x in cards_row2, cards_row1)
	if len(intersection) == 1:
		return intersection[0]
	elif len(intersection) == 0:
		return "Volunteer cheated!"
	else:
		return "Bad magician!"

with open("A-small-attempt0.out.txt", "w") as fr:
	with open("A-small-attempt0.in.txt", "r") as f:
		test_cases = int(f.readline())
		for test_num in xrange(test_cases):
			row1 = int(f.readline())
			cards1 = [map(int, f.readline().split(" ")) for x in xrange(4)]
			row2 = int(f.readline())
			cards2 = [map(int, f.readline().split(" ")) for x in xrange(4)]
			fr.write("Case #%s: %s\n" % (test_num + 1, solve(cards1[row1 - 1], cards2[row2 - 1])))

