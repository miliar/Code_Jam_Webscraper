lst = []

def operate(ls):
	lst = []
	while ls:
		if 'Z' in ls:
			ls.remove('Z')
			ls.remove('E')
			ls.remove('R')
			ls.remove('O')
			lst.append(0)
		elif 'W' in ls:
			ls.remove('T')
			ls.remove('W')
			ls.remove('O')
			lst.append(2)
		elif 'G' in ls:
			ls.remove('E')
			ls.remove('I')
			ls.remove('G')
			ls.remove('H')
			ls.remove('T')
			lst.append(8)
		elif 'X' in ls:
			ls.remove('S')
			ls.remove('I')
			ls.remove('X')
			lst.append(6)
		elif 'U' in ls:
			ls.remove('F')
			ls.remove('O')
			ls.remove('U')
			ls.remove('R')
			lst.append(4)
		elif 'T' in ls:
			ls.remove('T')
			ls.remove('H')
			ls.remove('R')
			ls.remove('E')
			ls.remove('E')
			lst.append(3)
		elif 'F' in ls:
			ls.remove('F')
			ls.remove('I')
			ls.remove('V')
			ls.remove('E')
			lst.append(5)
		elif 'S' in ls:
			ls.remove('S')
			ls.remove('E')
			ls.remove('V')
			ls.remove('E')
			ls.remove('N')
			lst.append(7)
		elif 'O' in ls:
			ls.remove('O')
			ls.remove('N')
			ls.remove('E')
			lst.append(1)
		else:
			ls.remove('N')
			ls.remove('I')
			ls.remove('N')
			ls.remove('E')
			lst.append(9)
	return lst

def main():
	T = int(input())
	for i in range(T):
		i += 1
		l = raw_input()
		ls = list(l)
		lst = operate(ls)
		lst.sort()
		l = ''.join(str(e) for e in lst)
		print 'Case #{}: {}'.format(i, l)

main()
