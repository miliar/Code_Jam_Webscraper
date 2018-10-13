#!/usr/bin/python
import sys, re, string, math

def do_one_case(cnum):
	N = int(sys.stdin.readline().strip())
	l = list()
	cross = {}
	ans = 0

	for i in range(N):
		(y1, y2) = map(int, sys.stdin.readline().split())
		l.append([y1,y2])
	
	for i in range(N-1):
		for j in range(i+1, N):
			if l[i][1] - l[i][0] == l[j][1] - l[j][0]:
				continue
			x = float(l[j][0] - l[i][0]) / (l[i][1] - l[i][0] - l[j][1] + l[j][0])
			if x <= 0 or x >= 1:
				continue
			y = (l[i][1] - l[i][0]) * x + l[i][0]
			
			if not cross.has_key((x, y)):
				cross[(x,y)] = 1
				ans += 1

	print "Case #%d: %d" % (cnum, ans)

def main():
	T = int(sys.stdin.readline().strip())
	for i in range(T):
		do_one_case(i+1)

if __name__ == "__main__":
	main()
