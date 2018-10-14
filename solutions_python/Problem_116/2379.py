i = open('A-large.in','r')
o = open('result.txt','w')
def testcases():
    n_cases = int(i.next().strip())
    print("n_cases: {n_cases}".format(**locals()))
    for x in range(n_cases):
        print(x)
        case = []
        for y in range(4):
            nxt = i.next()
            case.extend([c for c in nxt.strip()])
        print(case)
        yield case
        i.next()
           


def run():
    cases = [(i+1, c) for i, c in enumerate(testcases())]
    for i, case in cases:
        a = check_diagonals(case)
        b = check_horizontals(case)
	c = check_verticals(case)
	if any([a == 'X',b == 'X',c == 'X']):
	    o.write("Case #{i}: X won\n".format(**locals()))
	elif any([a == 'O', b == 'O', c == 'O']):
	    o.write("Case #{i}: O won\n".format(**locals()))
	else:
	    if "." in case:
		o.write("Case #{i}: Game has not completed\n".format(**locals()))
            else:
		o.write("Case #{i}: Draw\n".format(**locals()))


def check_diagonals(case):
    dia_1 = [case[0],case[5],case[10],case[15]]
    dia_2 = [case[3],case[6],case[9],case[12]]
    for dia in [dia_1,dia_2]:
	if all(["X" in d or "T" in d for d in dia]):
	    return "X"
	if all(["O" in d or "T" in d for d in dia]):
	    return "O"
    
def check_horizontals(case):
    lines = []
    for i in range(4):
	lines.append([case[0 + 4*i], case[1 + 4 * i], case[2 + 4 * i], case[3 + 4 * i]])
    for line in lines:
	if all([c == "O" or c == "T" for c in line]):
	    return "O"
	if all([c == "X" or c == "T" for c in line]):
	    return "X"
	

def check_verticals(case):
    lines = []
    for i in range(4):
	lines.append([case[0+i], case[4+i], case[8+i], case[12+i]])
    for line in lines:
	if all([c == "O" or c == "T" for c in line]):
	    return "O"
	if all([c == "X" or c == "T" for c in line]):
	    return "X"


run()
