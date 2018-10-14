def flip(S):
	length = len(S)
	for pancake in xrange(length):
		if S[pancake] == '+':
			S[pancake] = '-'
		else:
			S[pancake] = '+'
	return S

def pancakes(S):
	length = len(S)
	S_list = list(S)
	flips = 0
	
	if length == 1:
		if S_list[0] == '-':
			return 1
		else:
			return 0
	for i in xrange(length-1):
		if S_list[i] != S_list[i+1]:
			S_list = flip(S_list[:i+1]) + S_list[i+1:]
			flips += 1

	if S_list[0] == '-':
		S_list = flip(S_list)
		flips += 1
	return flips
	
#Get input
t = int(raw_input().strip())
tests = []
for _ in xrange(t):
    tests.append(raw_input().strip())

#do stuff
for i in xrange(t):
	flips = pancakes(tests[i])
	print "Case #{0}: {1}".format(i+1, flips)

