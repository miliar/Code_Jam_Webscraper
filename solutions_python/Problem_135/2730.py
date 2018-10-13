#first problem#
#sayf_piratos #
###############
import sys

sys.stdin, sys.stdout = map(open,"A-small-attempt1.in A-small-attempt1.out".split(" "), "r w+".split(" "))
cases_number = int(sys.stdin.readline())
for i in range(cases_number):
	user_answer1 = int(sys.stdin.readline())
	pattern1 = []
	pattern2 = []
	for j in range(4):
		pattern1.append(sys.stdin.readline().strip().split(" "))
	user_answer2 = int(sys.stdin.readline())
	for j in range(4):
		pattern2.append(sys.stdin.readline().strip().split(" "))
	answer = list(set(pattern1[user_answer1 - 1]) & set(pattern2[user_answer2 - 1]))
	if len(answer) == 0:
		sys.stdout.write( "Case #%d: Volunteer cheated!\n" %(i+1))
	elif len(answer) == 1:
		sys.stdout.write( "Case #%d: %s\n" %((i+1), answer[0]))
	else:
		sys.stdout.write("Case #%d: Bad magician!\n" %(i+1))
