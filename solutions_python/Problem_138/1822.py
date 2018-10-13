from collections import deque

cases = int(raw_input())

def parse(part):
	return int(float(part) * 100000 + 1e-9)


def play_war(naomi, ken):
	n = len(naomi)	
	used = [False] * n
	naomi_pt = 0

	for i in range(n):
		choice = -1
		choice_smallest_available = -1

		for j in range(n):
			if used[j] == False:
				if choice_smallest_available == -1:
					choice_smallest_available = j

				if naomi[i] < ken[j]:
					choice = j
					break

		if choice != -1:
			used[choice] = True
		else:
			used[choice_smallest_available] = True
			naomi_pt = naomi_pt + 1

	return naomi_pt



def play_deceitful_war(naomi, ken):
	n = len(naomi)	

	naomi_pt = 0
	naomi_idx, ken_idx = 0, n - 1
	nq = deque(naomi)
	kq = deque(ken)

	while len(nq) > 0:
		if kq[-1] < nq[-1]:
			naomi_pt = naomi_pt + 1
			nq.pop()
			kq.pop()
		else:	
			nq.popleft()
			kq.pop()

	
	return naomi_pt


def solve():
	n = int(raw_input())
	line = raw_input()
	naomi = map(parse, line.split(" "))
	ken = map(parse, raw_input().split(" "))

	naomi.sort()
	ken.sort()

	war = play_war(naomi, ken)
	deceitful_war = play_deceitful_war(naomi, ken)
	return deceitful_war, war


for case_no in xrange(1, cases+1):
	res = solve()
	print "Case #%d: %d %d" % (case_no, res[0], res[1])
