

with open("A-large.in", "r") as input:
    T = int(input.readline())
    for case in xrange(1, T+1):
    	m, s = input.readline().strip().split(' ')

    	friends = 0
    	standing = 0
    	for k in xrange(0,len(s)):
    		shyness = int(s[k])
    		if standing < k :
    			needed = k - standing
    			standing+= needed
    			friends+= needed

    		standing+= shyness
    	print "Case #"+str(case)+": "+str(friends)