

if __name__ == "__main__":
	N = int(raw_input())

	for case in range(1, N+1):
		s1, s2 = set(), set()

		l = int(raw_input()) - 1
		for u in range(4):
			line = raw_input()
			if u != l:
				continue
			s1 = set([ int(u) for u in line.split() ])

		l = int(raw_input()) - 1
		for u in range(4):
			line = raw_input()
			if u != l:
				continue
			s2 = set([ int(u) for u in line.split() ])

		s = list(s1.intersection(s2))

		if len(s) == 1:
			print "Case #" + str(case) + ": " + str(s[0])
		elif len(s) == 0:
			print "Case #" + str(case) + ": Volunteer cheated!"
		else:
			print "Case #" + str(case) + ": Bad magician!"

