f = open("A-large.in", 'r')
ou = open("out", 'w')
inlist = f.readlines()
L = int(inlist[0])
#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
def slnA(S, P):
	stand = P[0]
	count = 0
	for i in xrange(1, S + 1):
		if P[i] == 0:
			continue
		if i <= stand:
			stand += P[i]
		else:
			count += i - stand
			stand += i - stand
			stand += P[i]
	return str(count)

row = 1
for i in xrange(L):
	isl = inlist[row].split(' ')
	S = int(isl[0])
	P = [int(ch) for ch in isl[1] if ch != '\n']
	res = slnA(S, P)
	print res, S, P
	row += 1
	ou.write("Case #" + str(i + 1) + ": " + res + '\n')

f.close()
ou.close()