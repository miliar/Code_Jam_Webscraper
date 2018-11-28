import fileinput as f 

def deceit_score(naomi, ken):
	na = sorted(naomi)
	ke = sorted(ken)
	score = 0
	for n in ke:
		if n < popLeastGreatest(n,na):
			score +=1
	return score

def popLeastGreatest(n, a):
	for i in a:
		if i > n:
			a.remove(i)
			return i
	return a[0]

def war_score(naomi, ken):
	na = sorted(naomi)
	ke = sorted(ken)
	score = 0
	for n in na:
		if n > popLeastGreatest(n,ke):
			score +=1
	return score

def parse_input():
	cases  = 0
	case_n = 1
	naomi  = []
	ken    = []
	for x in f.input():
		if f.isfirstline():
			cases = int(x)
		elif case_n > cases:
			break
		else:
			j = (f.lineno() - 1) % 3
			if j is 1 and naomi:
				print "Case #%s: %s %s" % (case_n, deceit_score(naomi,ken), war_score(naomi,ken))
				case_n +=1
			elif j is 2:
				naomi = [float(x) for x in x.split()]
			else:
				ken = [float(x) for x in x.split()]
	print "Case #%s: %s %s" % (case_n, deceit_score(naomi,ken), war_score(naomi,ken))

parse_input()