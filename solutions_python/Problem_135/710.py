#
# Google Code Jam 2014
# Problem A: Magic Trick
# 
# Solved by Michael Oliver (a.k.a. The Code Boss)
# April 11, 2014
#

# Helpers
def ReadMatrix():
	out = []
	for i in range(0,4):
		lis = input().split()
		ints = list(map(lambda x: int(x), lis))
		out.append(ints)
	return out

# Main program
NumTests = int(input())

for TestNumber in range(1,NumTests+1):

	FirstRowAnswer = int(input())-1
	FirstMatrix = ReadMatrix()
	
	PossibleAnswers1 = set(FirstMatrix[FirstRowAnswer])
	
	SecondRowAnswer = int(input())-1
	SecondMatrix = ReadMatrix()
	
	PossibleAnswers2 = set(SecondMatrix[SecondRowAnswer])
	
	Answers = list(PossibleAnswers1.intersection(PossibleAnswers2))
	
	if len(Answers) > 1:
		Answer = 'Bad magician!'
	elif len(Answers) > 0:
		Answer = str(Answers[0])
	else:
		Answer = 'Volunteer cheated!'

	print('Case #%d: %s' % (TestNumber, Answer))