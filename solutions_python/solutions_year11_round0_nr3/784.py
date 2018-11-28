f = open('input')
g = open('output', 'w')
lines = f.readline()
lines = int(lines)

for i in range(0, lines):
	f.readline()
	case = f.readline()
	xor = eval(case.replace(" ", "^"));
	g.write("Case #{0}:".format(i + 1))
	if(xor):
		g.write(" NO\n")
	else:
		case = case.split()
		case = map(lambda x: int(x), case)
		case.sort()
		sean_gets = sum(case) - case[0]
		g.write(" {0}\n".format(sean_gets))
