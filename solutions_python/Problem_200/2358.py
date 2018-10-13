def findTidyNumber(n):
	strn = str(n)
	l = len(strn)
	# print l
	r = ''
	for i in range(l):
		c = strn[i]
		lastc = r[len(r) - 1] if len(r) > 0 else '0'
		for j in range(9, -1, -1):
			tempr = r + str(j) * (l - i)
			# print tempr
			itr = int(tempr)
			if (itr <= n):
				r += str(j)
				break


	return int(r)

# it starts here
import sys
l = sys.stdin.readline()
count = int(l)

results = []
for i in range(count) :
	n = sys.stdin.readline()
	n = int(n)
	results.append(findTidyNumber(n))

# print results
for i in range(count):
	print 'Case #' + str(i+1) + ": " + str(results[i])
