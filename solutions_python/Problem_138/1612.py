import sys
sys.setrecursionlimit(1500)
def get_rows(lines):
	if lines == 1:
		return map(float, raw_input().split())
	return [map(float, raw_input().split()) for _ in range(lines)]

def get_war(naomi, ken):
	if len(naomi) == 1:
		return 1 if naomi[0] > ken[0] else 0
	if ken[-1] > naomi[-1]:
		for idx, val in enumerate(ken):
			if val > naomi[-1]:
				return get_war(naomi[:-1], ken[:idx] + ken[(idx + 1):])
	else:
		return 1 + get_war(naomi[:-1], ken[1:])
	
def get_deceitful(naomi, ken):
	if len(naomi) == 1:
		return 1 if naomi[0] > ken[0] else 0
	if ken[0] > naomi[0] or ken[-1] > naomi[-1]:
		return get_deceitful(naomi[1:], ken[:-1])
	else:
		return 1 + get_deceitful(naomi[1:], ken[1:])

cases = input()

for i in range(1, cases + 1):
	input()
	naomi = sorted(get_rows(1))
	ken = sorted(get_rows(1))
	deceitful = get_deceitful(naomi, ken)
	war = get_war(naomi, ken)
	print "Case #{0}: {1} {2}".format(i, deceitful, war)

