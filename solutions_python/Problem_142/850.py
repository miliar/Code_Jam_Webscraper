T = int(raw_input())

results = []



for k in xrange(T):
	N = int(raw_input())
	strings = []
	for i in xrange(N):
		strings.append(str(raw_input()))
		strings[i] += "0"
	i = 0
	j = 0
	result = 0
	while i < len(strings[0]) and j < len(strings[1]):
#		print "i,j", i, j
		if j == 0:
			if strings[0][j] != strings[1][j]:
				result = -1
				break
			else:
				currentchar = strings[0][j]
				i += 1
				j += 1
		else:
			if strings[0][i] == currentchar:
				if strings[1][j] == currentchar:
					i += 1
					j += 1
				else:
					i += 1
					result += 1
			elif strings[1][j] == currentchar:
				if strings[0][i] == currentchar:
					i += 1
					j += 1
				else:
					j += 1
					result += 1
			elif strings[0][i] == strings[1][j]:
				currentchar = strings[0][i]
				i += 1
				j += 1
			else: #neither string's char is equal to currentchar, and neither string's char are equal
				result = -1
#				print strings[0][i], strings[1][j]
#				print "nothing equal"
				break
		if result == -1:
			break
#		print "result:", result
#		print "currentchar:", currentchar
#	print "i,j", i, j
	if result != -1:
		while i < len(strings[0]):
			if strings[0][i] == currentchar:
				result += 1
				i += 1
			else:
				result = -1
				break
		while j < len(strings[1]):
			if strings[1][j] == currentchar:
				result += 1
				j += 1
			else:
				result = -1
				break
	results.append(result)

"""
for k in xrange(T):
	if results[k] == -1:
		print "Case #{}: Fegla Won".format(k+1)
	else:
		print "Case #{}: {}".format(k+1, results[k])
"""

f = open("TheRepeaterOut.txt", 'w')
for k in xrange(T):
	if results[k] == -1:
		print >> f, "Case #{}: Fegla Won".format(k+1)
	else:
		print >> f, "Case #{}: {}".format(k+1, results[k])
f.close()
