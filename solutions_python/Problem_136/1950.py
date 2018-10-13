def run(i, o):
	cases = int(i.readline())
	case = 0
	while case < cases:
		case+=1
		income = 2
		total = 0
		c, f, x = [float(n) for n in i.readline().split()]
		while True:
			t = c/income
			total += t
			if (x-c)/income < x/(income+f):
				total += (x-c)/income
				break
			else:
				income += f
		o.write("Case #{}: {}".format(case, total))
		if case != cases:
			o.write("\n")


def main():
	file_name = "B-large"
	i = open(file_name+".in", 'r')
	o = open(file_name+".out", 'w')
	run(i, o)


main()

