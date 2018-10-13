vowels = ('a', 'e', 'i', 'o', 'u')
def found(chip):
	for letter in chip:
		if letter in vowels:
			return True
	return False

for T in xrange(input()):
	name, n = [x for x in raw_input().split()]
	n = int(n)
	name += ' '
	record = set()
	i = 0
	while i <= len(name)-n:
		if name[i + n - 1] in vowels:
			i += n
			continue
		if not found(name[i: i+n]):
			reduce(lambda _,y: record.add(y), [ (j,k) for j in xrange(0,i+1) for k in xrange(i+n,len(name))],tuple())
		i += 1
	print "Case #%d:"%(T+1), len(record)
	# print "|    ",sorted(record)

