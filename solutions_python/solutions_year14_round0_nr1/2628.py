import sys

lines = sys.stdin.readlines()

T = int(lines.pop(0))

def load_ans():
	first_ans = int(lines.pop(0))

	ret = ""
	for i in range(0,4):
		if (i+1) == first_ans:
			ret = lines.pop(0)
		else:
			lines.pop(0)

	return set([int(x) for x in ret.strip().split(" ")])
def ans(s):
	if len(s) == 1:
		return s.pop()
	elif len(s) == 0:
		return "Volunteer cheated!"
	else:
		return "Bad magician!"

for i in range(0, T):
	first_answer = load_ans()
	second_answer = load_ans()

	print "Case #%d: %s" % (i+1, ans(first_answer & second_answer))
