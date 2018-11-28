f = open('A-large.in', 'r')
o = open('1.out', 'w')

T = int(f.readline().strip())



for t in xrange(T):
	p = map(str, f.readline().strip().split(' '))
	NeededFriends = 0
	standingPeople = 0
	n = 0
	for char in p[1]:
		if int(char)>0:
			if standingPeople >= n:
				standingPeople = standingPeople + int(char) 
			else:
				NeededFriends = NeededFriends +  ( n - standingPeople )
				standingPeople = standingPeople + (n - standingPeople ) + int(char)
		n = n+1
		
	o.write("Case #" + str(t+1) + ": " + str(NeededFriends) + "\n")
print "done"