import sys

N = int(sys.stdin.readline().strip())
cards1 = {}
cards2 = {}
for t in range(N):
	#print "Problem", t+1
	r1 = int(sys.stdin.readline().strip())-1
	#print r1
	for i in range(4):
		l = sys.stdin.readline().strip()
		cards1[i] = l.split(" ")

	#print cards1
	r2 = int(sys.stdin.readline().strip())-1
	#print r2
	for i in range(4):
		l = sys.stdin.readline().strip()
		cards2[i] = l.split(" ")

	#print cards2

	out = [val for val in cards1[r1] if val in cards2[r2]]

	if len(out) == 1:
		res = out[0]
	elif len(out) == 0:
		res = "Volunteer cheated!"
	else:
		res = "Bad magician!"

	print "Case #{0}: {1}".format(t+1, res)