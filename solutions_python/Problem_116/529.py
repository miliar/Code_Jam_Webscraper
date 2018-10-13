import io
import sys


def check(m, sx, sy, vx, vy):
	n1 = 0
	n2 = 0
	rangex = [sx]
	for i in range(3):
		rangex.append(rangex[i] + vx)
	rangey = [sy]
	for i in range(3):
		rangey.append(rangey[i] + vy)
	for x, y in zip(rangex, rangey):
		if m[x][y] >= 0 and m[x][y] <= 1:
			n1 += 1
		if m[x][y] <= 0:
			n2 += 1
	if n1 == 4:
		return 'X'
	if n2 == 4:
		return 'O'
	return ''


def decide(x):
	for I in range(4):
		res = check(x, 0, I, 1, 0)
		if res:
			return res
	for I in range(4):
		res = check(x, I, 0, 0, 1)
		if res:
			return res
	res = check(x, 0, 0, 1, 1)
	if res:
		return res
	res = check(x, 0, 3, 1, -1)
	if res:
		return res
	return ''

def main():
	inf = open('in.txt', 'r', encoding='utf-8')
	outf = open('out.txt', 'w', encoding='utf-8')
	#outf = sys.stdout
	
	first_line = inf.readline()
	print(first_line)
	T = int(first_line.rstrip())
	for i in range(T):
		has_empty = False
		x = [[] for j1 in range(4)]
		for j in range(4):
			line = inf.readline().rstrip()
			#print(line)
			for c in line:
				if c == 'X':
					x[j].append(1)
				elif c == 'O':
					x[j].append(-1)
				elif c == 'T':
					x[j].append(0)
				elif c == '.':
					x[j].append(1000)
					has_empty = True
		l = inf.readline()
		#print(x)
		
		res = decide(x)
		print('Case #' + str(i + 1) + ': ', end='', file=outf)
		if not res:
			if has_empty:
				print('Game has not completed', file=outf)
			else:
				print('Draw', file=outf)
		else:
			print(res + ' won', file=outf)

if __name__ == '__main__':
	main()