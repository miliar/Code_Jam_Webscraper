

t = int(raw_input())
order = "1023456789abcdefghijklmnopqrstuvwxyz"

for i in xrange(t):
	word = raw_input()

	convert = {}
	final = ""
	j = 0

	for k in word:
		if convert.has_key(k):
			final += convert[k]
		else:
			convert[k] = order[j]
			j += 1
			final += convert[k]
	if j<2:
		j=2
	print "Case #"+str(i+1)+":",int(final,j)

