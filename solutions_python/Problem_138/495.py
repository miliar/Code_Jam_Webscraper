def main(filepath):
	f = open(filepath, 'r')
	out = open('war_out.txt', 'w')
	num_cases = int(f.readline())
	for i in range(num_cases):
		naomi, ken = parse_game(f)
		deceitful = optimal_deceit(naomi, ken)
		truthful = optimal_truthful(naomi, ken)
		out.write('Case #%d: %d %d' % (i+1, deceitful, truthful))
		if i < num_cases - 1:
			out.write('\n')

def parse_game(f):
	blocks = int(f.readline())
	naomi = sorted(map(float, f.readline().split()))
	ken = sorted(map(float, f.readline().split()))
	return naomi, ken

def optimal_truthful(naomi, ken):
	naomi = map(lambda x: (x, 'N'), naomi)
	ken = map(lambda x: (x, 'K'), ken)
	combined = map(lambda x: x[1], sorted(naomi+ken, key=lambda x: x[0]))
	# print naomi, ken
	maximum = 0
	current = 0
	while combined:
		current = current + 1 if combined.pop() == 'N' else current - 1
		maximum = max(current, maximum)
	return maximum

def optimal_deceit(naomi, ken):
	naomi = naomi[:]
	ken = ken[:]
	score = 0
	while naomi:
		if naomi[-1] > ken[-1]:
			score += 1
			naomi.pop()
			ken.pop()
		else:
			naomi.pop(0)
			ken.pop()
	return score

main('D-large.in')


