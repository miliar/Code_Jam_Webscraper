import sys

T = int(sys.stdin.readline())

for case in range(1, T+1):
	sys.stdout.write("Case #" + str(case) + ": ")
	row1 = []
	row2 = []
	
	row1n = int(sys.stdin.readline())
	for r in range(1,5):
		tmp = map(int,sys.stdin.readline().split())
		if row1n == r:
			row1 = tmp
	
	row2n = int(sys.stdin.readline())
	for r in range(1, 5):
		tmp = map(int,sys.stdin.readline().split())
		if row2n == r:
			row2 = tmp
			
	# intersection
	inters = set(row1).intersection(row2)
	if len(inters) == 1:
		print iter(inters).next()
	elif len(inters) == 0:
		print "Volunteer cheated!"
	else:
		print "Bad magician!"

