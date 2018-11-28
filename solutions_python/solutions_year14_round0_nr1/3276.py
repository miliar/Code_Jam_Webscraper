import sys

rl = lambda: sys.stdin.readline()
n = int(rl())
for i in range(n):

	ans1 = int(rl().strip())
	counter = 1
	for j in range(4):
		output = rl().strip()
		if(ans1 == counter):
			arr1 = output.split(' ')
		counter += 1
			
	counter = 1
	ans2 = int(rl().strip())
	for j in range(4):
		output = rl().strip()
		if(ans2 == counter):
			arr2 = output.split(' ')
		counter += 1

	intsec = list(set(arr1) & set(arr2))
	
	if len(intsec) == 1:
		result = "%s" % (' ').join(intsec)
	elif len(intsec) > 1:
		result = "Bad magician!"
	else :
		result = "Volunteer cheated!"

	print "Case #%d: %s" % (i+1, result)