
def getInput(path):
        f = open(path)
        lines = f.readlines()
        f.close()
        return lines

def print_output():
	lines = getInput("./input")
	no_cases = int(lines[0].strip())
	case = 1
	while (case<=no_cases):
		items = lines[case].split()
		C = float(items[0])
		F = float(items[1])
		X = float(items[2])
		remainingX = X;
		doneTime = 0;
		n = 0;
		while(True):
			xequator =  C*(2+F*float(n)+F)/F;
			xn = 0;
			success = False;
			if remainingX <= xequator:
				xn = remainingX;
				success = True;
			else:
				xn = C;
			doneTime += xn/(2+(F*n));
			if success:
				break;
			n += 1;
		print "Case #{0}: {1}".format(case,doneTime)
		case += 1;

print_output()