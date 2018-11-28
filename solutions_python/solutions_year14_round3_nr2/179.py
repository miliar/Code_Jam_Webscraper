import itertools
import re

def _valid(cars, chars):
	s = "".join(cars)

	for c in chars:
		fi = s.find(c)
		la = s.rfind(c, fi)

		sli = s[fi:la+1]

		if len(set(sli)) > 1:
			return False

	return True


in_file = open("B-small-attempt1.in")
out_file = open("B-small-attempt1.out", "wt")
cases = {}

n_cases = int(in_file.readline())
n = 0
case = 0

for line in in_file:
	line = line.rstrip()

	n += 1

	if n % 2 != 0:
		continue

	case += 1
	answer = None

	splitted = line.split()
	cars = []
	chars = set()
	ok = 0

	for spl in splitted:
		for c in set(spl):
			spl = re.sub(c + "+", c, spl)
		
		cars.append(spl)

	all_chars = set("".join(cars))
	txt = "".join(cars)

	for c in all_chars:
		if txt.count(c) > 1:
			chars.add(c)

	for p in itertools.permutations(cars):
		if _valid(p, chars):
			ok += 1

	answer = ok

	print("Case #%s: %s" % (case, answer))
	out_file.write("Case #%s: %s\n" % (case, answer))

in_file.close()
out_file.close()