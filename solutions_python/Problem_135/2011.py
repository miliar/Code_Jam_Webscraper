def pick_cards(i, o):
	t = int(i.readline())
	case = 0
	while case < t:
		case += 1
		g1 = int(i.readline())
		o1 = []
		for _ in range(4):
			o1.append(i.readline().split())
		g2 = int(i.readline())
		o2 = []
		for _ in range(4):
			o2.append(i.readline().split())

		possible = set(o1[g1-1]) & set(o2[g2-1])
		if len(possible) == 0:
			result = "Volunteer cheated!"
		elif len(possible) == 1:
			result = list(possible)[0]
		else:
			result = "Bad magician!"
		o.write("Case #{}: {}".format(case, result))
		if case != t:
			o.write("\n")

def main():
	file_name = "A-small-attempt0"

	i = open(file_name+".in", 'r')
	o = open(file_name+".out", 'w')
	pick_cards(i, o)


main()

