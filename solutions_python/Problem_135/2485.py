import sys
#import fileinput
#for line in fileinput.input():
#	process(line)

f = open(sys.argv[1])

cases = int(f.readline())
#print cases

for x in range(0, cases):

	sq_pre = []
	sq_post = []

	row_pre = int(f.readline())
	#print row_pre
	for r in range (0, 4):
		numbers = [int(n) for n in f.readline().split(' ')]
		#print numbers
		sq_pre.append(numbers)

	row_post = int(f.readline())
	#print row_post
	for r in range (0, 4):
		numbers = [int(n) for n in f.readline().split(' ')]
		#print numbers
		sq_post.append(numbers)

	# SING NOW!
	candidates = []
	for number in sq_pre[row_pre-1]:
		if number in sq_post[row_post - 1]:
			candidates.append(number)

	#print candidates
	print 'Case #%d:' % (x+1),
	if len(candidates) == 1:
		print candidates[0]
	elif len(candidates) < 1:
		print 'Volunteer cheated!'
	elif len(candidates) > 1:
		print 'Bad magician!'

f.close()

