#!/usr/bin/env python3

def parse():
	n, p = map(int, input().split())
	l = map(int, input().split())
	return l, p

def solve(l, p):
	l = [x%p for x in l]
	c = [l.count(i) for i in range(p)]
	if p==2:
		return c[0] + c[1]//2 + ((c[1]%2)!=0)
	if p==3:
		m1 = min(c[1],c[2])
		m2 = max(c[1],c[2])
		return c[0] + m1 + (m2-m1)//3 + (((m2-m1)%3)!=0)
	if p==4:
		m1 = min(c[1],c[3])
		m2 = max(c[1],c[3])
		if c[2]%2==1 and m2-m1>=2:
			return c[0] + c[2]//2 + m1 + 1 + (m2-m1-2)//4 + (((m2-m1-2)%4)!=0)
		elif c[2]%2==1 and m2==m1:
			return c[0] + c[2]//2 + m1 + 1
		else:
			return c[0] + c[2]//2 + m1 + (m2-m1)//4 + (((m2-m1)%4)!=0)

def main():
	for i in range(int(input())):
		l, p = parse()
		s = solve(l, p)
		print('Case #{}: {}'.format(i+1, s))

if __name__ == '__main__': main()