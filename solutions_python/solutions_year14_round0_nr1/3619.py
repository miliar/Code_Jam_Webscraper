from sets import Set
import sys

argList = sys.argv
filename = argList[1]
f = file(filename, 'r')
out = file('output.txt', 'w')
lines = f.readlines()
cases = int(lines[0])
lines = lines[1:]

for case in range(1, cases+1):
	problemSet = lines[0:10]
	lines = lines[10:]
	ans1 = int(problemSet[0])
	board1 = problemSet[1:5]
	ans2 = int(problemSet[5])
	board2 = problemSet[6:]

	outcome1 = board1[ans1-1].strip().split(' ')
	outcome2 = board2[ans2-1].strip().split(' ')

	inter = Set(outcome1).intersection(outcome2)

	if (len(inter) == 0) :
		out.write("Case #" + str(case) + ": Volunteer cheated!\n")
	elif (len(inter) > 1) :
		out.write("Case #" + str(case) + ": Bad magician!\n")
	else:
		num = list(inter)[0]
		out.write("Case #" + str(case) + ": " + str(num) + "\n")


