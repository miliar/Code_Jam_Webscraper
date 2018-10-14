import fileinput


def last_tidy(n):
	i = 0
	for i in xrange(len(n)-1):
		x = n[i]
		y = n[i+1]
		if x > y:
			n[i] = x - 1
			for j in xrange(i+1, len(n)):
				n[j] = 9
			
			# Since n[i] is now one less, then n[i-1] could be larger than n[i]
			j = i
			while j > 0:
				if n[j-1] > n[j]:
					n[j] = 9
					n[j-1] = n[j-1] -1
					j -= 1
				else:
					break
			
			break
			
	n = map(str, n)
	n = ''.join(n)
	return int(n)
			
	
it = fileinput.input()
it.next()
num = 1
for line in it:
	n = list(line.strip("\n"))
	n = map(int, n)
	print "Case #" + str(num) + ': ' + str(last_tidy(n))
	num += 1
	
	
	