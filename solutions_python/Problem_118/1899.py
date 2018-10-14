import math
pas = raw_input()
for i in range(int(pas)):
	count = 0
	args = raw_input()
	args = args.split(' ')
	min = int(args[0])
	max = int(args[1])+1
	for a in range(min, max):
		sRoot = math.sqrt(a)
		aRoot = int(int(sRoot) % sRoot)
		if aRoot == 0:
			if str(a) == str(a)[::-1] and str(int(sRoot)) == str(int(sRoot))[::-1]:
				count += 1
	
	print 'Case #' + str(i+1) + ': ' + str(count)