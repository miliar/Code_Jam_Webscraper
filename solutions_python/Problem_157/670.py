#-*- coding: utf-8 *-*
def third(a, b):
	ijk = set(["i", "j", "k"])
	return ijk.difference(set([a,b])).pop()

def ijk_poryadok(a, b):
	if a == "i":
		if b == "j":
			return True
		else:
			return False
	elif a == "j":
		if b == "k":
			return True
		else:
			return False
	elif a == "k":
		if b == "i":
			return True
		else:
			return False


def mult(s):
	if len(s) != 2:
		sys.stderr.write("Error!")
	else:
		if s[0] == s[1]:
			return "", -1
		if ijk_poryadok(s[0], s[1]) == True:
			return third(s[0], s[1]), 1
		else:
			return third(s[0], s[1]), -1

t = int(raw_input(""))
for t_ in range(1,t+1):
	l, x = raw_input("").split(" ")
	l = int(l)
	x = int(x)
	s = raw_input("")*x
	chetnost = 1
	i = ""
	j = ""
	while len(i + j + s) > 3:
		if not i:
			if s[0] == "i":
				i = "i"
				s = s[1:]
		if i and not j:
			if s[0] == "j":
				j = "j"
				s = s[1:]
		part, cur_chet = mult(s[:2])
		chetnost *= cur_chet
		s = part + s[2:]
	if chetnost == 1 and i + j + s == "ijk":
		print "Case #%s: YES" % t_
	else:
		print "Case #%s: NO" % t_
	#print chetnost, i + j + s


