# t = input()

def non_desc(i):

	i = str(i)
	if len(i) == 1:
		return True
	else:
		first = i[0]
		for n in i[1:]:
			if n < first:
				return False
			first = n
		return True

def solve_stupid(n):
	for i in xrange(n, 0, -1):
		if non_desc(i):
			return str(i)
	raise Exception("wrong!")


def solve_smart(n):
	n = str(n)
	# first find decreasing spot!
	dspot = -1
	if n[0] == "0":
		dspot = 0

	f = n[0]
	for idx in xrange(len(n)):
		if n[idx] < f:
			dspot = idx
			break
		else:
			f = n[idx]

	if dspot == -1:
		return n

	dspot2 = -1
	curNum = None
	for idx in xrange(dspot-1, -1, -1):

		if curNum == None and n[idx] > "1":
			dspot2 = idx
			curNum = str(int(n[idx]) - 1)
		else:
			if n[idx] <= curNum:
				dspot2 = idx + 1
				break
			else:
				dspot2 = idx

	if dspot2 == -1:
		return "9"*(len(n) -1)
	res = n[:dspot2] + str((int(n[dspot2]) - 1))
	res += (len(n) - len(res))*"9"

	return str(int(res))



t = input()
for i in xrange(t):
	n = input()
	print "Case #{0}: {1}".format(i+1, solve_smart(n))
	
