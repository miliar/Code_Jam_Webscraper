import sys

T = int(sys.stdin.readline().strip())

for i in range(T):
	answer1 = int(sys.stdin.readline().strip())
	possibilities1 = set()
	for j in range(4):
		if j+1 == answer1:
			map(possibilities1.add,sys.stdin.readline().strip().split(" "))
		else: 
			sys.stdin.readline()
	answer2 = int(sys.stdin.readline().strip())
	possibilities2 = set()
	for j in range(4):
		if j+1 == answer2:
			map(possibilities2.add,sys.stdin.readline().strip().split(" "))
		else: 
			sys.stdin.readline()
	answers = [p for p in possibilities1.intersection(possibilities2)]
	out = "Volunteer cheated!"
	if len(answers) == 1: out = answers[0]
	elif len(answers) > 1: out = "Bad magician!"
	print "Case #%d: %s" % (i+1,out)
