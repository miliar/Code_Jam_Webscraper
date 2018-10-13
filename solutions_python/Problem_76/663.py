from collections import *

def main():
	global c,o
	inp = open('input', 'r')
	out = open('output', 'w')
	g = []
	n = 1
	for row in inp:
		g = row.split()
		l = len(g)
		if(l>1):
			a=[]
			i=0
			s = 0
			while(i<l):
				a.append(int(g[i]))
				s = s^a[i]
				i = i+1
			if(not(s)):	ans = sum(a) - min(a)
			else:	ans = 'NO'
			st = str(ans)
			out.write('Case #')
			t = str(n)
			out.write(t)
			out.write(': ')
			out.write(st)
			out.write('\n')
			n = n+1
	return 0

if __name__ == '__main__':
	main()
