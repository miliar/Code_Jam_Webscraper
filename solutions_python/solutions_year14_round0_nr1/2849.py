import sys
def intersection(row1, row2):
	return list(set(row1) & set(row2))

def find_card(a1, arr1, a2, arr2):
	# answer 1, array 1, answer 2, array 2
	row1, row2 = arr1[a1-1], arr2[a2-1]
	inter = intersection(row1, row2)
	if len(inter) < 1:
		return 'Volunteer cheated!'
	if len(inter) > 1:
		return 'Bad magician!'
	return inter[0]

f = open(sys.argv[1])
N = int(f.readline().strip())
for case in xrange(1, N+1):
	a1 = int(f.readline().strip())
	arr1 = []
	for i in xrange(4):
		arr1.append(map(int ,f.readline().strip().split(" ")))
	a2 = int(f.readline().strip())
	arr2 = []
	for i in xrange(4):
		arr2.append(map(int, f.readline().strip().split(" ")))
	print "Case #%s: %s" %(case, find_card(a1, arr1, a2, arr2))

	
	
