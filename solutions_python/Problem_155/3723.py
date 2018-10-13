import string

T = int(raw_input())

Cases = [ [] for i in xrange(T) ]

for i in xrange(T):
	NewInput = raw_input()
	newInput = NewInput.split()

	Number = int(newInput[0])

	Cases[i].append(Number)

	for j in xrange(Number+1):
		Numbers = newInput[1]
		Cases[i].append(int(Numbers[j]))


Results = [None]*T

for i in xrange(T):
	Number = Cases[i][0]
	Max = 0
	Sum = 0
	for j in xrange(Number+1):
		Max = max(Max, j-Sum)
		Sum += Cases[i][j+1]
	Results[i] = Max

for i in xrange(T):
	string = "Case #%d: %d" %(i+1, Results[i])
	print string

