#!/usr/bin/python
f = open('input', 'r')
w = open('output', 'w')

n_cases = f.readline()
print "cases:" + n_cases

cases = f.read().splitlines()
n_case = 1
for case in cases:
	prob = case.split(" ")
	smax = prob[0]
	print "smax: " + smax

	standing = 0
	friends = 0
	i=0
	for p in prob[1]:
		print "s" + str(i) + ": " + p 
		if int(p) > 0 and i > 0 and standing < i:
			friends += i - standing
			standing += friends

		standing += int(p)
		
		print "standing " + str(standing)
		print "friends: " + str(friends)

		i+=1
	
	print "--"
	print "Case #" +  str(n_case) + ": " + str(friends)
	print "--"

	if n_case < int(n_cases):
		w.write("Case #" +  str(n_case) + ": " + str(friends) + "\n")
	else:
		w.write("Case #" +  str(n_case) + ": " + str(friends))

	n_case += 1
f.closed
w.closed