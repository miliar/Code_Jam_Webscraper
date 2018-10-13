#!/usr/bin/python3

def pal(x):
	s = str(x)
	return s == s[::-1]

L = []

for i in range(1, 10**5):
	a = int(str(i) + str(i)[::-1])
	b = int(str(i) + str(i)[-2::-1])
	if(pal(a*a)):
		L.append(a*a)
	if(pal(b*b)):
		L.append(b*b)

cases = int(input())
for q in range(1, cases+1):
	line = input().split()
	A = int(line[0])
	B = int(line[1])
	n = 0
	for i in L:
		if A <= i and i <= B:
			n += 1
	print("Case #%d: %d" % (q, n))
