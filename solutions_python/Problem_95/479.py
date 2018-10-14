from string import maketrans 

intab  = "ynficwlbkuomxsevzpdrjgthaq"
outtab = "abcdefghijklmnopqrstuvwxyz"

trantab = maketrans(intab, outtab)


def translate(line):
	return line.strip().translate(trantab)

def solve():
	with open('A-small-attempt1.in') as f:
		data = f.readlines()
	with open('A-small-1.out', 'w') as o:
		for i, line in enumerate(data[1:]):
			o.write("Case #%d: %s\n" % (i + 1, translate(line)))

if __name__ == '__main__':
	solve()
