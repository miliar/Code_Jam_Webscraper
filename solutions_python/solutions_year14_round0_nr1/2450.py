import sys

def test(test_num, f):
	a1 = int(f.readline()) - 1
	s1 = [
		[int(j) for j in f.readline().split(' ')]
		for i in range(4)
	]
	a2 = int(f.readline()) - 1
	s2 = [
		[int(j) for j in f.readline().split(' ')]
		for i in range(4)
	]
	answers = [i for i in s2[a2] if i in s1[a1]]
	if len(answers) == 0:
		print("Case #%d: Volunteer cheated!" % test_num)
	elif len(answers) == 1:
		print("Case #%d: %d" % (test_num,answers[0]))
	else:
		print("Case #%d: Bad magician!" % test_num)

def tests(f):
	n = int(f.readline())
	for i in range(n):
		test(i + 1, f)

#with open("input.txt") as f:
#	tests(f)
tests(sys.stdin)
