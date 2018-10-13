import pdb

file = open('A-large.in', 'r')
n = int(file.readline())
for index in range(n):
	length = int(file.readline().strip())
	line = file.readline().strip().split(' ')
	x = [int(j) for j in line]
	s1 = 0
	speed = 0
	for i in range(len(x)-1):
		if x[i] > x[i+1]:
			s1 = s1 + x[i] - x[i+1]
			if x[i] - x[i+1] > speed:
				speed = x[i] - x[i+1]

	s2 = 0
	for i in range(len(x)-1):
		if x[i] == 0:
			s2 = s2
		elif x[i] <= speed:
			s2 = s2 + x[i]
		else:
			s2 = s2 + speed
	print "Case #%s: %s" % (str(index+1), str(s1)+' '+str(s2))
    
