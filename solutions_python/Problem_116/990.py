#!/usr/bin/python3

def main():
	f = open('../test_files/input', 'r')
	w = open('../test_files/output', 'w')
	s = f.readline()
	t = int(s)
	for i in range(1, t+1):
		w.write('Case #%d: ' % i)
		a = []
		for j in range(4):
			a.append(list(f.readline())[:-1])
		f.readline()
		result = find(a)
		if result == 'X':
			w.write('X won\n')
		elif result == 'O':
			w.write('O won\n')
		elif result == '?':
			w.write('Draw\n')
		else:
			w.write('Game has not completed\n')
	w.close()

def find(a):
	for i in range(4):
		xw = True
		ow = True
		for j in range(4):
			if a[i][j] == '.': break
			if a[i][j] == 'T': continue
			if a[i][j] == 'X': ow = False
			if a[i][j] == 'O': xw = False
			if not (xw or ow): break
		else:
			return 'X' if xw else 'O'
	for j in range(4):
		xw = True
		ow = True
		for i in range(4):
			if a[i][j] == '.': break
			if a[i][j] == 'T': continue
			if a[i][j] == 'X': ow = False
			if a[i][j] == 'O': xw = False
			if not (xw or ow): break
		else:
			return 'X' if xw else 'O'
	xw = True
	ow = True
	for i in range(4):
		if a[i][i] == '.': break
		if a[i][i] == 'T': continue
		if a[i][i] == 'X': ow = False
		if a[i][i] == 'O': xw = False
		if not (xw or ow): break
	else:
		return 'X' if xw else 'O'
	xw = True
	ow = True
	for i in range(4):
		if a[i][3-i] == '.': break
		if a[i][3-i] == 'T': continue
		if a[i][3-i] == 'X': ow = False
		if a[i][3-i] == 'O': xw = False
		if not (xw or ow): break
	else:
		return 'X' if xw else 'O'
	return '.' if '.' in reduce(list.__add__, a) else '?'

if __name__ == '__main__':
	main()
