T = int(raw_input())

global results
results = []

for i in xrange(T):
	row1 = int(raw_input()) - 1
	A = []
	for i in xrange(4):
		A.append(map(int, raw_input().split()))
	possibilities = A[row1]

	row2 = int(raw_input()) - 1
	result = []
	B = []
	for i in xrange(4):
		B.append(map(int, raw_input().split()))
	for i in xrange(4):
		for j in xrange(4):
			if B[row2][i] == possibilities[j]:
				result.append(B[row2][i])
				break
	results.append(result)

"""
for i in xrange(T):
	if len(results[i]) == 0:
		print "Case #{}: Volunteer cheated!".format(i+1)
	elif len(results[i]) == 1:
		print "Case #{}: {}".format(i+1,int(results[i]))
	elif len(results[i]) > 1:
		print "Case #{}: Bad magician!".format(i+1)
"""
f = open("MagicTrickOut.txt", 'w')
for i in xrange(T):
	if len(results[i]) == 0:
		print >> f, "Case #{}: Volunteer cheated!".format(i+1)
	elif len(results[i]) == 1:
		print >> f, "Case #{}: {}".format(i+1,int(results[i][0]))
	elif len(results[i]) > 1:
		print >> f, "Case #{}: Bad magician!".format(i+1)
f.close()
