

nTests = input()

for i in xrange(nTests):
	[ maxShyness, people ] = map( lambda x : x.strip(), raw_input().split(' ') )
	maxShyness = int(maxShyness)
	people = [ int(shyCount) for shyCount in people ]
	additional = 0
	standing = people[0]
	for required in xrange(1, maxShyness + 1):
		if standing < required:
			additional += (required - standing)
			standing = required
		standing += people[required]
	print 'Case #%d: %d' % (i + 1, additional)