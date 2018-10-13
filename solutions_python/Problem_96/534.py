import sys

def google_dancers(s):
	
	x = s.split()
	x = [int(x[i]) for i in range(len(x))]
	n = x.pop(0)
	sn = x.pop(0)
	p = x.pop(0)
	sc = 0
	t=0
	for i in range(len(x)):
		marks = x[i]
		if marks == 0 and p != 0:
			continue
		if marks >= (3*p - 4):
			if marks % 3 == 2:
				q = marks/3
				a = marks - p
				if a%2 == 0 and q < p:
					sc += 1
			elif marks % 3 == 0:
				if marks/3 < p:
					sc += 1
			t += 1
	if sc-sn > 0:
		return t - (sc-sn)
	return t

if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
    lines =[line.strip() for line in open(fn)]
    lines.pop(0)
    
    for line in range(len(lines)):
		print "Case #"+str(line+1)+": "+str(google_dancers(lines[line]))
