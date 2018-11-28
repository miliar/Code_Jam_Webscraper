#!python

def main():
	f = open('../test_files/input', 'r')
	w = open('../test_files/output', 'w')
	t = int(f.readline())
	for i in range(1, t+1):
		w.write("Case #%d: " % i)
		#r, ma = [int(x) for x in f.readline().split()]
		n = int(f.readline())
		strings = []
		for j in range(n):
			strings.append(f.readline().rstrip())
		strings = [a1(s) for s in strings]
		res = a2(strings)
		if res is None:
			w.write("Fegla Won\n")
		else:
			w.write("%d\n" % res)

def a1(q):
	symb = None
	u = []
	for s in q:
		if symb is None:
			symb = s
			u = [[symb, 1]]
		elif s == symb:
			u[-1][1] += 1
		else:
			symb = s
			u.append([symb, 1])
	return u

def a2(strings):
	le = len(strings[0])
	for st in strings[1:]:
		if len(st) != le:
			return None
	dev = 0
	for i in range(le):
		sy = strings[0][i][0]
		s = strings[0][i][1]
		for st in strings[1:]:
			if sy != st[i][0]:
				return None
			s += st[i][1]
		r = s // len(strings)
		for st in strings:
			dev += abs(st[i][1] - r)
	return dev

if __name__ == "__main__":
	main()