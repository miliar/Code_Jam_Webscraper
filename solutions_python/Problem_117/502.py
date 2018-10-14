import io
import sys


def check(m, sx, sy):
	val = m[sx][sy]
	ok = True
	for i in range(len(m)):
		if m[i][sy] > val:
			ok = False
			break
	if ok:
		return True
	ok = True
	for j in range(len(m[0])):
		if m[sx][j] > val:
			ok = False
			break
	if ok:
		return True
	return False


def decide(x):
	for i in range(len(x)):
		for j in range(len(x[0])):
			if not check(x, i, j):
				return False
	return True
	

def main():
	inf = open('in.txt', 'r', encoding='utf-8')
	outf = open('out.txt', 'w', encoding='utf-8')
	#outf = sys.stdout
	
	first_line = inf.readline()
	print(first_line)
	T = int(first_line.rstrip())
	for test in range(T):
		N, M = inf.readline().rstrip().split()
		N = int(N)
		M = int(M)
		x = [[] for j1 in range(N)]
		for i in range(N):
			line = inf.readline().rstrip().split()
			for tok in line:
				x[i].append(int(tok))
		#print(x)
		
		res = decide(x)
		print('Case #' + str(test + 1) + ': ', end='', file=outf)
		if res:
			print('YES', file=outf)
		else:
			print('NO', file=outf)

if __name__ == '__main__':
	main()