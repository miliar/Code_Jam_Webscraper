numOfCases = int(raw_input())

def regular_war(naomi, ken):
	score_naomi = 0
	for n in naomi:
		ken, score = ken_move(n, ken)
		score_naomi += score
	return score_naomi

def deceitful_war(naomi, ken):
	score_naomi = 0
	for n in naomi:
		if n > ken[0]:
			ken, score = ken_move(ken[-1]+0.001, ken)
		else:
			ken, score = ken_move(ken[-1]-0.001, ken)
		score_naomi += score
	return score_naomi

def ken_move(n, ken):
	for k in ken:
		if k > n:
			ken.remove(k)
			return (ken, 0)
	ken = ken[1:]
	return (ken, 1)



for caseNum in range(1, numOfCases+1):
	raw_input()
	naomi = sorted([float(num) for num in raw_input().split(" ")])
	ken = sorted([float(num) for num in raw_input().split(" ")])

	print "Case #%d: %d %d" % (caseNum, deceitful_war(naomi[:], ken[:]), regular_war(naomi[:], ken[:]))