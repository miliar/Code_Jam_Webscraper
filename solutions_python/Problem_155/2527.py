f = open("AL.in", "r")

test_cases = int(f.readline())

for x in xrange(test_cases):
	standing = 0
	
	case = map(int, list(f.readline().split(" ")[1][:-1]))
	friends = 0
	
	for _ in xrange(len(case)):
		if case[_] == 0:
			continue
		
		if standing >= _:
			standing += case[_]
		
		else:
			friends += _ - standing
			standing = _ + case[_]
	
	print "Case #{}: {}".format(x + 1, friends)